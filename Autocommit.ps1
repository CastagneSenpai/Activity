# Create a modification
Set-Location "E:\_dev\04-Scripts Powershell\Activity"
$date = Get-Date
Add-Content "README.md" "`n Mise a jour du $date"

# Git commands to update Github
git add .
git commit -m "Mise a jour quotidienne du $date"
git push