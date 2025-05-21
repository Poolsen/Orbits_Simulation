#todo: Möglichkeit für importieren von vorgefertigten Szenarien importieren
#todo: alten Code entfernen und durch create_moving_Objects ersetzen, damit code tatsächlich Funktionalität hat

import config
from Satellites_Calculations import MovingObject
from Visuals import Visualisierung

weiteres_Objekt: bool = True        #kp warum, aber wenn man :bool entfernt kommt fucking type error; dont worry be happy
moving_objects: list = []

# nur temporary: irgendwie schlau ändern // edit: temporary mein ass
print("Gib als erstes das Zentral - Objekt an, das du erstellen möchtest! Dies sollte das größte Objekt sein und erhält eine andere Farbe!")


while weiteres_Objekt:
    name = input("Name: ")
    mass = input("Mass: ")
    x = input("X-Koordinate: ")
    y = input("Y-Koordinate: ")

    try:
        x, y = float(x), float(y)

    except ValueError as e:
        print(
            f"Du muss eine Zahl mit *Punkt* als Komma eingeben! Sie darf keine Rechenoperation enthalten! Fehlercode: {e}")
    except Exception as e:
        print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")

    try:
        mass = float(mass)

    except ValueError as e:
        print(f"Du muss eine Zahl mit Punkt als Komma eingeben! Sie darf keine Rechenoperation enthalten! Fehlercode: {e}")
    except Exception as e:
        print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")

    new_moving_object = MovingObject(x, y, mass)

    if len(moving_objects) == 0:    # Zentral-Teil
        new_Visual_object = Visualisierung(config.hellblau, 30)

    else:
        new_Visual_object = Visualisierung(config.weiss, 20)

    moving_objects.append((new_moving_object, new_Visual_object)) # klammer wichtig, um als tuple zu passen



    if input("Drücke Enter für ein weiteres Objekt! ") == "":
        weiteres_Objekt = True
    else:
        weiteres_Objekt = False

#Debugging - funktioniert: Es wird jedes Mal ein neues Objekt erstellt mit eigenen Attributen und Memory - Allocations
"""for n in range(len(moving_objects)):
    print(moving_objects[n].x)
for n in moving_objects:
    print(n.x)"""
# beide optionen möglich zum Iterieren!
