Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete

# Autocompletion for arrow keys
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