# installed packages: pygame

# Path to your virtual environment
venv_path = r"venv\Scripts\activate_this.py" #das ist der Pfad, um zu activate_this.py zu kommen und es dann auszuführen, was dann das venv startet --> packages verfügbar

# Activate the virtual environment
with open(venv_path) as file_:
    exec(file_.read(), {'__file__': venv_path})

import pygame       #nur um zu überprüfen, ob das venv wirklich gestartet wird: wenn nicht bricht das programm schon hier ab, da pygame nicht gefunden wird (nur im venv installiert)

print("Hello World")

n = 100

while n == 100:
    n = input("n = ")
