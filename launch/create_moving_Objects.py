import config
from launch import preset_handler

def init_simulation():
    return create(way_of_creation())


def way_of_creation():
    return input("Wie soll die Simulation geladen werden?\n"
            "'p' -> Presets\n"
            "'l' -> legacy - version\n").lower().strip()

def create(way) -> list:
    while (type(way) == str) is False:
        way = way_of_creation()

    if way == "l":
        return init_moving_objects_legacy()
    else:
        return preset_handler.read_preset_data()

def init_moving_objects_legacy() -> list:

    moving_objects: list = []

    # nur temporary: irgendwie schlau ändern // edit: temporary für immer
    first_input: str = input("Gib als erstes das Zentral - Objekt an, das du erstellen möchtest! Dies sollte das größte Objekt sein und erhält eine andere Farbe! Drücke Enter! ")


    # Möglichkeit für presets:
    do_else = True

    if len(first_input) > 0 and first_input[0] == "/":
        match first_input[1:]:
            case "Sonnensystem":
                from Satellites_Calculations import MovingObject
                from Visuals import Visualisierung
                erde = MovingObject(0, 0, 5.972 * 10 ** 24)
                erde.planet = True
                erde_vis = Visualisierung(config.hellblau, 30)

                s1 = MovingObject(-36000 * 1000, 0, 1000)
                s1.y_v = 3.1 * 1000  # 3.1 km/s --> 3100 m/s
                s1_vis = Visualisierung(config.weiss, 20)

                moving_objects.append((erde, erde_vis))
                moving_objects.append((s1, s1_vis))

                do_else = False

            case _:
                pass

    # Möglichkeit für das Erstellen ganz neuer Objekte
    if do_else:
        n = 1
        weiteres_objekt = True
        moving_objects: list = []
        all_args: dict = {}

        while weiteres_objekt:
            mass = input("Masse [kg]: ")
            x = input("X-Koordinate [m]: ")
            y = input("Y-Koordinate [m]: ")
            y_v = input("Startgeschwindigkeit nach unten [m/s]: ")
            x_v = input("Startgeschwindigkeit nach rechts [m/s]: ")

            try:
                if x == "":
                    x = 0
                else:
                    x = float(eval(x))

                if y == "":
                    y = 0
                else:
                    y = float(eval(y))

                if y_v == "":
                    y_v = 0
                else:
                    y_v = float(eval(y_v))

                if x_v == "":
                    x_v = 0
                else:
                    x_v = float(eval(x_v))

                if mass == "":
                    mass = 0
                else:
                    mass = float(eval(mass))

            except ValueError as e:
                print(
                    f"Du muss eine Zahl mit *Punkt* als Komma eingeben!"
                    f"Sie darf  Rechenoperation (/ ; *; **) enthalten! Fehlercode: {e}")
                continue

            except Exception as e:
                print(
                    "Du muss eine Zahl mit *Punkt* als Komma eingeben! "
                    "Sie darf  Rechenoperation (/ ; *; **) enthalten!")

                print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")
                continue

            args_one_object = {
                "x": x,
                "y": y,
                "mass": mass,
                "x_v": x_v,
                "y_v": y_v,
                "id": len(all_args)
            }

            all_args[f"object no.: {n}"] = args_one_object
            n += 1

            match input("Weiteres Objekt hinzufügen?\n"
                        "Ja (' ') \n"
                        "Nein ('n')\n"
                        ""):
                case "n" | "N" | "m" | "M":
                    weiteres_objekt = False

                case _:
                    pass

        from Satellites_Calculations import MovingObject
        from Visuals import Visualisierung

        for n in range(len(all_args)):
            new_moving_object = MovingObject(all_args[f"object no.: {n+1}"].get("x"),
                                             all_args[f"object no.: {n+1}"].get("y"),
                                             all_args[f"object no.: {n+1}"].get("mass"))

            new_moving_object.x_v = all_args[f"object no.: {n+1}"].get("x_v")
            new_moving_object.y_v = all_args[f"object no.: {n+1}"].get("y_v")

            if all_args[f"object no.: {n+1}"]["id"] == 0:  # Zentral-Teil

                new_visual_object = Visualisierung(config.hellblau, 30)

            else:
                new_visual_object = Visualisierung(config.weiss, 20)

            moving_objects.append((new_moving_object, new_visual_object))  # klammer wichtig, um als tuple zu passen

    return moving_objects


#Debugging - funktioniert: Es wird jedes Mal ein neues Objekt erstellt mit eigenen Attributen und Memory - Allocations

"""for n in range(len(moving_objects)):
    print(moving_objects[n].x)
for n in moving_objects:
    print(n.x)
for n in a:
    print(n[0].x)
    print(n[1].farbe)
    """
# beide optionen möglich zum Iterieren!
