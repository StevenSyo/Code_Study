# 使用当前目录作为工作路径
$folderPath = (Get-Location).Path  # 获取当前所在的目录路径

# 获取所有以 l- 开头的文件（这些是预设的用户名单）
$listFiles = Get-ChildItem -Path $folderPath -Filter "l-*.csv"

foreach ($listFile in $listFiles) {
    # 将 l- 文件名转换成对应的 r- 文件名（实际的机器名单）
    $realFileName = $listFile.Name -replace "^l-", "r-"
    $realFilePath = Join-Path $folderPath $realFileName  # 生成实际名单文件的完整路径

    # 检查是否存在对应的实际名单文件，如果没有则报错提示但继续执行
    if (-Not (Test-Path $realFilePath)) {
        Write-Warning "Matching real file not found: $realFileName"
        Write-Host "[ERROR] Real file not found for: $($listFile.Name)" -ForegroundColor Red
        continue
    }

    # 从 list 文件中读取用户字段（去掉空格）
    $listUsers = Import-Csv $listFile.FullName | ForEach-Object { $_.user.Trim() }
    # 从 real 文件中读取用户字段（去掉空格）
    $realUsers = Import-Csv $realFilePath | ForEach-Object { $_.user.Trim() }

    # 合并两个用户列表并去重，用于后续比较
    $allUsers = ($listUsers + $realUsers) | Sort-Object -Unique

    $result = @()  # 初始化结果列表
    foreach ($user in $allUsers) {
        if ($listUsers -contains $user -and $realUsers -contains $user) {
            $status = "same"  # 两边都有，表示一致
        } elseif ($listUsers -contains $user) {
            $status = "-"      # 只在 list 有，表示需要删除
        } else {
            $status = "+"      # 只在 real 有，表示需要新增
        }
        $result += "$user,$status"  # 合并用户名与状态，加入结果中
    }

    # 构造新文件名，将 l- 改为 d-，表示 diff 文件
    $outputFileName = $listFile.Name -replace "^l-", "d-"
    $outputFilePath = Join-Path $folderPath $outputFileName  # 生成输出文件完整路径

    $output = @("user,status") + $result  # 构造输出内容，添加表头
    Set-Content -Path $outputFilePath -Value $output -Encoding UTF8  # 写入新文件

    Write-Host "Written: $outputFileName"  # 输出提示信息
}
