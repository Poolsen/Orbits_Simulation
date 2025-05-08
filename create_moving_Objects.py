import config
from Satellites_Calculations import MovingObject

weiteres_Objekt: bool = True
moving_objects = []

while weiteres_Objekt:
    name = input("Name: ")

    mass = input("Mass: ")
    x = input("X-Koordinate: ")
    y = input("Y-Koordinate: ")

    try:
        x, y = float(x), float(y)

    except ValueError as e:
        print(
            f"Du muss eine Zahl mit Punkt als Komma eingeben! Sie darf keine Rechenoperation enthalten! Fehlercode: {e}")
    except Exception as e:
        print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")


    new_moving_object = MovingObject(x, y, mass)

    moving_objects.append(new_moving_object)

    try:
        mass = float(mass)

    except ValueError as e:
        print(f"Du muss eine Zahl mit Punkt als Komma eingeben! Sie darf keine Rechenoperation enthalten! Fehlercode: {e}")
    except Exception as e:
        print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")

    if input("Drücke Enter für ein weiteres Objekt! ") == "":
        weiteres_Objekt = True
    else:
        weiteres_Objekt = False

for n in range(len(moving_objects)):
    print(moving_objects[n].x)
for n in moving_objects:
    print(n.x)

# beide optionen möglich zum iteraten!
