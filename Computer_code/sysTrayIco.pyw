from infi.systray import SysTrayIcon
import subprocess
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_main_program(systray=None):
    script_path = os.path.join(BASE_DIR, "__main__.py")
    subprocess.Popen([sys.executable, script_path], cwd=BASE_DIR)

menu_options = (
    ("Run Main Program", None, run_main_program),
)

systray = SysTrayIcon(r"Icos\telePhone.ico", "Cracked Deck", menu_options)

# Run once automatically on startup
run_main_program()

# And keep tray icon running
systray.start()