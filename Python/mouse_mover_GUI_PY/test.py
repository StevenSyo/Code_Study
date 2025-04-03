import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import pyautogui
import datetime
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import sys
import os

class MouseMoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动鼠标移动器")
        self.root.geometry("360x300")
        self.root.resizable(False, False)

        self.running = False
        self.end_time = None
        self.interval = 2  # 秒

        self._create_widgets()

    def _create_widgets(self):
        self.option = tk.StringVar(value="duration")

        self.radio_duration = ttk.Radiobutton(self.root, text="运行时长（分钟）", variable=self.option, value="duration")
        self.radio_duration.pack(anchor=tk.W, padx=20, pady=5)
        self.entry_duration = ttk.Entry(self.root)
        self.entry_duration.pack(fill=tk.X, padx=20)

        self.radio_start_end = ttk.Radiobutton(self.root, text="指定开始/结束时间（格式 HH:MM）", variable=self.option, value="time")
        self.radio_start_end.pack(anchor=tk.W, padx=20, pady=5)

        self.label_start = ttk.Label(self.root, text="开始时间：")
        self.label_start.pack(anchor=tk.W, padx=20)
        self.entry_start = ttk.Entry(self.root)
        self.entry_start.pack(fill=tk.X, padx=20)

        self.label_end = ttk.Label(self.root, text="结束时间：")
        self.label_end.pack(anchor=tk.W, padx=20)
        self.entry_end = ttk.Entry(self.root)
        self.entry_end.pack(fill=tk.X, padx=20)

        self.btn_start = ttk.Button(self.root, text="开始运行", command=self.start_timer)
        self.btn_start.pack(pady=10)

        self.label_countdown = ttk.Label(self.root, text="剩余时间：00:00:00", font=("Arial", 14))
        self.label_countdown.pack(pady=5)

        self.btn_quit = ttk.Button(self.root, text="退出程序", command=self.exit_app)
        self.btn_quit.pack(pady=5)

    def start_timer(self):
        if self.running:
            return

        mode = self.option.get()
        now = datetime.datetime.now()

        if mode == "duration":
            try:
                minutes = float(self.entry_duration.get())
                self.end_time = now + datetime.timedelta(minutes=minutes)
            except ValueError:
                messagebox.showerror("错误", "请输入有效的分钟数")
                return
        else:
            try:
                start_str = self.entry_start.get()
                end_str = self.entry_end.get()
                start_time = datetime.datetime.combine(now.date(), datetime.datetime.strptime(start_str, "%H:%M").time())
                end_time = datetime.datetime.combine(now.date(), datetime.datetime.strptime(end_str, "%H:%M").time())
                if now < start_time:
                    delay = (start_time - now).total_seconds()
                    self.root.after(int(delay * 1000), lambda: self._start_movement(end_time))
                    messagebox.showinfo("等待中", f"将在 {start_str} 开始运行")
                    return
                else:
                    self._start_movement(end_time)
                    return
            except Exception as e:
                messagebox.showerror("错误", f"时间格式错误：{e}")
                return

        self._start_movement(self.end_time)

    def _start_movement(self, end_time):
        self.end_time = end_time
        self.running = True
        threading.Thread(target=self._run_loop, daemon=True).start()
        self._update_countdown()
        self._setup_tray_icon()

    def _run_loop(self):
        while self.running and time.time() < self.end_time.timestamp():
            pyautogui.moveRel(10, 0)
            time.sleep(0.2)
            pyautogui.moveRel(-10, 0)
            time.sleep(self.interval)

        self.running = False
        self.label_countdown.config(text="已完成。")
        messagebox.showinfo("完成", "鼠标移动已完成。")

    def _update_countdown(self):
        if not self.running:
            return
        remaining = int(self.end_time.timestamp() - time.time())
        if remaining < 0:
            remaining = 0
        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        self.label_countdown.config(text=f"剩余时间：{hours:02}:{minutes:02}:{seconds:02}")
        self.root.after(1000, self._update_countdown)

    def _setup_tray_icon(self):
        image = Image.new('RGB', (64, 64), color='black')
        draw = ImageDraw.Draw(image)
        draw.rectangle((16, 16, 48, 48), fill='white')
        self.tray_icon = pystray.Icon("mouse_mover", image, "自动鼠标移动器", menu=pystray.Menu(
            item('显示窗口', self._show_window),
            item('退出', self.exit_app)
        ))
        threading.Thread(target=self.tray_icon.run, daemon=True).start()
        self.root.protocol("WM_DELETE_WINDOW", self._hide_window)

    def _hide_window(self):
        self.root.withdraw()

    def _show_window(self):
        self.root.after(0, self.root.deiconify)

    def exit_app(self):
        self.running = False
        try:
            self.tray_icon.stop()
        except:
            pass
        self.root.destroy()


if __name__ == '__main__':
    if not hasattr(sys, 'frozen'):
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()