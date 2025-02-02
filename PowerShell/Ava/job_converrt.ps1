<#---------------------------------------------------------------------------       
機能名:　   LogConvert      
機能概要:   カスタムログをSJIS→UTF-8に文字コード変換します        
作成日:　   2023/9/13       
----------------------------------------------------------------------------#>      
#コンフィグファイル格納場所      
$ConfigPath = "E:\Tools\Scripts\LogConvert_Config.csv"
$LogFilesPath = "E:\Tools\Scripts\LogFiles_Config.csv"
#更新ファイルの時間設定        
$currentTime = Get-Date     
$previousTime = $currentTime.AddMinutes(-5)     
$previousTimevalue = "5"        
#Configからのリスト読み込み       
$List = import-csv -path $ConfigPath
$JobFiles = import-csv -path $LogFilesPath | Select-Object -ExpandProperty Jobdb
# 定数の定義
$logName = Application
$logSource = "ログ文字コード変換"
$eventId = 12345
$typeInf = Information
#更新があったファイルを検索
$UpdateFile = Get-ChildItem -Path $List.OrgLog_Dir -Recurse -File | Where-Object { $_.LastWriteTime -gt $previousTime }     
#更新ファイルがない場合　(全フォルダ一括チェック)
if ($UpdateFile.Count -eq 0) {
write-EventLog -LogName $logName -Source $logSource -EntryType $typeInf -EventID $eventId -Message "No Jobdb_files updated in the last 5 minutes."
exit
}
#更新ファイルがある場合（コンバート処理の開始）        
foreach($i in $List){
$UpdateFile = Get-ChildItem -Path $i.OrgLog_Dir -Recurse -File | Where-Object { $_.LastWriteTime -gt $previousTime }        
foreach ($file in $UpdateFile) {
if ($file.Extension -eq ".log" -or $file.Extension -eq ".txt" -or $file.Extension -eq ".csv") {
try {
#ファイルのコンバート
$content = Get-Content -ErrorAction Stop -Encoding Default -Path $file.FullName
Set-Content -Force -Path "$($i.TmpLog_Dir)`\$($file.Name)" -Value $content -Encoding UTF8
$result = echo $?
Write-EventLog -LogName $logName -Source $logSource -EventId $eventId -EntryType $typeInf -Message "info： $($file.Name) ファイルの UTF-8 へのコンバートが完了しました。（1/3）"
#コンバートしたファイルのコピー
Copy-Item -Force -Path "$($i.TmpLog_Dir)`\$($file.Name)" -Destination "$($i.ConvertLog_Dir)`\$($file.Name)" -ErrorAction Stop
Write-EventLog -LogName $logName -Source $logSource -EventId $eventId -EntryType $typeInf -Message "info： $($file.Name) ファイルのファイルコピー処理が完了しました。（2/3）"
#コンバートしたファイルの削除
Remove-Item -Force -Path "$($i.TmpLog_Dir)`\$($file.Name)" -ErrorAction Stop
Write-EventLog -LogName $logName -Source $logSource -EventId $eventId -EntryType $typeInf -Message "info： $($file.Name) ファイルのコピー元を削除しました。（3/3）"
                } catch {
$errorMessage = "error:Error converting $($file.Name) to UTF-8 encoding: $_"
#Write-Host $errorMessage
Write-EventLog -LogName $logName -Source $logSource -EventId $eventId -EntryType Error -Message $errorMessage
                }
            }
        }
    }
