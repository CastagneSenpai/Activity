# Change to your repository directory
Set-Location "E:\_dev\04-Scripts Powershell\Activity"

# Récupérer la date actuelle
$date = Get-Date

# Ajouter une ligne au fichier README.md
Add-Content "README.md" "`n Mise a jour du $date"

# Ajouter le fichier au prochain commit
git add .

# Commit avec un message
git commit -m "Mise a jour quotidienne du $date"

# Pousser les changements vers GitHub
git push