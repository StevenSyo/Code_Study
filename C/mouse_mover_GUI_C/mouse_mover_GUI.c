#include <windows.h>
#include <commctrl.h>
#include <stdio.h>
#include <wchar.h>
#include <time.h>

#pragma comment(lib, "comctl32.lib")

int running = 0;
int paused = 0;
HWND hLabel, hPauseBtn, hStartBtn, hStopBtn;
int remaining_seconds = 0;
time_t start_time = 0, end_time = 0;
HANDLE hCountdownThread = NULL;
HANDLE hMouseThread = NULL;

DWORD WINAPI countdown(LPVOID lpParam) {
    while (running && remaining_seconds >= 0) {
        if (!paused) {
            int h = remaining_seconds / 3600;
            int m = (remaining_seconds % 3600) / 60;
            int s = remaining_seconds % 60;

            wchar_t buffer[64];
            swprintf(buffer, 64, L"剩余时间：%02d:%02d:%02d", h, m, s);
            SetWindowTextW(hLabel, buffer);

            Sleep(1000);
            remaining_seconds--;
        } else {
            Sleep(500);
        }
    }
    if (running) {
        SetWindowTextW(hLabel, L"任务完成。\n");
        MessageBoxW(NULL, L"鼠标移动任务完成！", L"完成", MB_OK | MB_ICONINFORMATION);
    }
    running = 0;
    return 0;
}

DWORD WINAPI moveMouseThread(LPVOID lpParam) {
    POINT p;
    while (running && remaining_seconds > 0) {
        if (!paused) {
            GetCursorPos(&p);
            SetCursorPos(p.x + 10, p.y);
            Sleep(500);
            SetCursorPos(p.x, p.y);
            Sleep(500);
        } else {
            Sleep(500);
        }
    }
    return 0;
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    static HWND hInput, hStartHour, hStartMin, hEndHour, hEndMin;

    switch (msg) {
    case WM_CREATE:
        CreateWindowW(L"STATIC", L"开始时间(HH:MM)：", WS_VISIBLE | WS_CHILD,
            20, 10, 130, 20, hwnd, NULL, NULL, NULL);
        hStartHour = CreateWindowW(L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_NUMBER,
            150, 10, 30, 20, hwnd, NULL, NULL, NULL);
        hStartMin = CreateWindowW(L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_NUMBER,
            190, 10, 30, 20, hwnd, NULL, NULL, NULL);

        CreateWindowW(L"STATIC", L"结束时间(HH:MM)：", WS_VISIBLE | WS_CHILD,
            20, 40, 130, 20, hwnd, NULL, NULL, NULL);
        hEndHour = CreateWindowW(L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_NUMBER,
            150, 40, 30, 20, hwnd, NULL, NULL, NULL);
        hEndMin = CreateWindowW(L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_NUMBER,
            190, 40, 30, 20, hwnd, NULL, NULL, NULL);

        CreateWindowW(L"STATIC", L"或手动设定运行时长(分钟)：", WS_VISIBLE | WS_CHILD,
            20, 70, 200, 20, hwnd, NULL, NULL, NULL);
        hInput = CreateWindowW(L"EDIT", L"", WS_VISIBLE | WS_CHILD | WS_BORDER | ES_NUMBER,
            230, 70, 40, 20, hwnd, NULL, NULL, NULL);

        hStartBtn = CreateWindowW(L"BUTTON", L"开始", WS_VISIBLE | WS_CHILD,
            280, 70, 60, 24, hwnd, (HMENU)1, NULL, NULL);

        hPauseBtn = CreateWindowW(L"BUTTON", L"暂停", WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
            280, 100, 60, 24, hwnd, (HMENU)2, NULL, NULL);

        hStopBtn = CreateWindowW(L"BUTTON", L"停止", WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
            280, 130, 60, 24, hwnd, (HMENU)3, NULL, NULL);

        hLabel = CreateWindowW(L"STATIC", L"剩余时间：00:00:00", WS_VISIBLE | WS_CHILD,
            20, 100, 250, 24, hwnd, NULL, NULL, NULL);
        break;

    case WM_COMMAND:
        if (LOWORD(wParam) == 1 && !running) { // 启动任务
            wchar_t buf[16];
            GetWindowTextW(hInput, buf, 16);
            int duration = _wtoi(buf);

            if (duration > 0) {
                remaining_seconds = duration * 60;
            } else {
                wchar_t sh[8], sm[8], eh[8], em[8];
                GetWindowTextW(hStartHour, sh, 8);
                GetWindowTextW(hStartMin, sm, 8);
                GetWindowTextW(hEndHour, eh, 8);
                GetWindowTextW(hEndMin, em, 8);

                int shour = _wtoi(sh), smin = _wtoi(sm);
                int ehour = _wtoi(eh), emin = _wtoi(em);

                if ((shour | smin | ehour | emin) == 0 && duration <= 0) {
                    MessageBoxW(hwnd, L"请填写开始/结束时间或运行分钟数。", L"错误", MB_OK);
                    return 0;
                }

                time_t now = time(NULL);
                struct tm tstart = *localtime(&now);
                struct tm tend = tstart;

                tstart.tm_hour = shour;
                tstart.tm_min = smin;
                tstart.tm_sec = 0;

                tend.tm_hour = ehour;
                tend.tm_min = emin;
                tend.tm_sec = 0;

                start_time = mktime(&tstart);
                end_time = mktime(&tend);

                if (end_time <= start_time) {
                    MessageBoxW(hwnd, L"结束时间必须晚于开始时间。", L"错误", MB_OK);
                    return 0;
                }

                remaining_seconds = (int)(end_time - start_time);
            }

            running = 1;
            paused = 0;
            SetWindowTextW(hPauseBtn, L"暂停");
            hCountdownThread = CreateThread(NULL, 0, countdown, NULL, 0, NULL);
            hMouseThread = CreateThread(NULL, 0, moveMouseThread, NULL, 0, NULL);
        } else if (LOWORD(wParam) == 2 && running) { // 暂停/恢复
            paused = !paused;
            SetWindowTextW(hPauseBtn, paused ? L"继续" : L"暂停");
        } else if (LOWORD(wParam) == 3) { // 停止按钮
            running = 0;
            paused = 0;
            SetWindowTextW(hPauseBtn, L"暂停");
            SetWindowTextW(hInput, L"");
            SetWindowTextW(hStartHour, L"");
            SetWindowTextW(hStartMin, L"");
            SetWindowTextW(hEndHour, L"");
            SetWindowTextW(hEndMin, L"");
            SetWindowTextW(hLabel, L"剩余时间：00:00:00");
        }
        break;

    case WM_DESTROY:
        running = 0;
        PostQuitMessage(0);
        break;
    }
    return DefWindowProcW(hwnd, msg, wParam, lParam);
}

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance,
    LPWSTR lpCmdLine, int nCmdShow) {

    WNDCLASSW wc = { 0 };
    wc.lpfnWndProc = WndProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = L"MouseMoverWindow";
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);

    RegisterClassW(&wc);

    HWND hwnd = CreateWindowW(L"MouseMoverWindow", L"自动鼠标移动器",
        WS_OVERLAPPEDWINDOW & ~WS_THICKFRAME & ~WS_MAXIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT, 380, 230, NULL, NULL, hInstance, NULL);

    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);

    MSG msg;
    while (GetMessageW(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessageW(&msg);
    }
    return 0;
}
