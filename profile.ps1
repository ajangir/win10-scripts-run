# Autocompletion for arrow keys
Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete
Set-PSReadlineKeyHandler -Key UpArrow -Function HistorySearchBackward
Set-PSReadlineKeyHandler -Key DownArrow -Function HistorySearchForward
function bcp{
    git pull --rebase --autostash
    git add -A
    git commit -m "repo backup: $(date "+%F %R")"
    git push
}

function gs{
    git status
}

function keepass-merge{
    $sourceWin10 = 'C:\Users\ajay-winX\Music\keepass_all\mainKeysDB.kdbx'
    $destAndroid = 'C:\Users\ajay-winX\a_src\github\obs-root\.github\keepassxc-db\mainKeysDB.kdbx'
    $keepassCli = 'C:\Program Files\KeePassXC\keepassxc-cli.exe'
    & $keepassCli merge $sourceWin10 $destAndroid -s
    copy -verbose $sourceWin10 $destAndroid
    bcp
}