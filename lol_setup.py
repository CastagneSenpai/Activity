import subprocess
import time
import pygetwindow as gw
from pywinauto import Desktop

# Démarre les applications
subprocess.Popen(r"D:\Programmes\Riot Games\Riot Client\RiotClientServices.exe")
subprocess.Popen([
    r"D:\Program Files (x86)\Overwolf\OverwolfLauncher.exe",
    "-launchapp",
    "pibhbkkgefgheeglaeemkkfjlhidhcedalapdggh"
])
subprocess.Popen(r"C:\Users\rcasta911e\AppData\Local\Discord\Update.exe")

# Temps pour s'assurer que les applications sont bien lancées
time.sleep(15)

# Fonction pour déplacer les fenêtres vers le second écran
def move_to_second_screen(window_title):
    try:
        # Récupère la fenêtre par son titre
        window = gw.getWindowsWithTitle(window_title)[0]
        
        # Dimensions de l'écran principal pour le décalage
        primary_screen_width = Desktop(backend="win32").screens()[0]['width']
        
        # Déplace la fenêtre au second écran (à droite de l'écran principal)
        window.moveTo(primary_screen_width + 50, 50)  # Ajuste les valeurs pour le positionnement exact
    except IndexError:
        print(f"Fenêtre '{window_title}' non trouvée.")

# Déplace les fenêtres spécifiques
move_to_second_screen("Discord")
