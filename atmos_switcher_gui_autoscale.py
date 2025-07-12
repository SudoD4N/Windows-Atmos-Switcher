
import tkinter as tk
import subprocess
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

def run_game_mode():
    subprocess.Popen("control mmsys.cpl", shell=True)
    info_label.config(text="🎮  Stelle im Lautsprecher-Setup auf 7.1 um.")

def run_kino_mode():
    subprocess.Popen("start ms-settings:sound", shell=True)
    info_label.config(text="🎬  Aktiviere in den Einstellungen 'Dolby Atmos for Home Theater'.")

BG_COLOR = "#1f1b2e"
BTN_COLOR = "#f7633a"
BTN_HOVER = "#d94e2e"
BTN_TEXT = "#ffffff"
INFO_COLOR = "#7fe6dc"
TITLE_COLOR = "#ffffff"

app = tk.Tk()
app.title("Atmos Switcher")
app.configure(bg=BG_COLOR)
app.resizable(True, True)
app.columnconfigure(0, weight=1)

title = tk.Label(app, text="🎮🎬 ATMOS SWITCHER", font=("Segoe UI", 18, "bold"), fg=TITLE_COLOR, bg=BG_COLOR)
title.grid(row=0, column=0, pady=(20, 10), padx=20)

btn_game = tk.Button(app, text="🎮 Game-Modus (7.1 PCM)", font=("Segoe UI", 13), fg=BTN_TEXT, bg=BTN_COLOR,
                     activebackground=BTN_HOVER, width=30, command=run_game_mode, relief="flat", cursor="hand2")
btn_game.grid(row=1, column=0, pady=10, padx=20)

btn_kino = tk.Button(app, text="🎬 Kino-Modus (Dolby Atmos)", font=("Segoe UI", 13), fg=BTN_TEXT, bg=BTN_COLOR,
                     activebackground=BTN_HOVER, width=30, command=run_kino_mode, relief="flat", cursor="hand2")
btn_kino.grid(row=2, column=0, pady=10, padx=20)

info_label = tk.Label(app, text="", font=("Segoe UI", 10), fg=INFO_COLOR, bg=BG_COLOR)
info_label.grid(row=3, column=0, pady=(10, 20))

app.mainloop()
