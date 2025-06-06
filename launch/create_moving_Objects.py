#todo: Möglichkeit für importieren von vorgefertigten Szenarien importieren

import config


def init_moving_objects() -> list:

    weiteres_objekt: bool = True        #kp warum, aber wenn man :bool statt : bool macht kommt fucking type error; dont worry be happy
    moving_objects: list = []
    all_args = []

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

    # Möglichkeit für das Erstellen ganz neuer Objekte
    if do_else:
        while weiteres_objekt:
            name = input("Name: ")
            mass = input("Masse [kg]: ")
            x = input("X-Koordinate [m]: ")
            y = input("Y-Koordinate [m]: ")
            y_v = input("Startgeschwindigkeit nach unten [m/s]: ")
            x_v = input("Startgeschwindigkeit nach oben [m/s]: ")

            try:
                x, y = float(x), float(y)
                name = str(name)

                if y_v == "":
                    y_v = 0
                else:
                    y_v = float(y_v)

                if x_v == "":
                    x_v = 0
                else:
                    x_v = float(x_v)

            except ValueError as e:
                print(f"Du muss eine Zahl mit *Punkt* als Komma eingeben! Sie darf keine Rechenoperation (/ ; *; ^) enthalten! Fehlercode: {e}")
                continue
            except Exception as e:
                print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")
                continue

            try:
                mass = float(mass)

            except ValueError as e:
                print(f"Du muss eine Zahl mit Punkt als Komma eingeben! Sie darf keine Rechenoperation enthalten! Fehlercode: {e}")
                continue
            except Exception as e:
                print(f"Es gab einen unerwarteten, kritischen Fehler! Fehlercode {e}")
                continue

            args_one_object = {
                "name": name,
                "x": x,
                "y": y,
                "mass": mass,
                "x_v": x_v,
                "y_v": y_v,
                "id": len(all_args)
            }

            all_args.append(args_one_object)


            if input("Drücke Enter für ein weiteres Objekt! ") == "":
                weiteres_objekt = True
            else:
                weiteres_objekt = False

    from Satellites_Calculations import MovingObject
    from Visuals import Visualisierung

    for n in range(len(all_args)):
        new_moving_object = MovingObject(all_args[n].get("x"), all_args[n].get("y"), all_args[n].get("mass"))
        new_moving_object.x_v = all_args[n].get("x_v")
        new_moving_object.y_v = all_args[n].get("y_v")

        if n == 0:  # Zentral-Teil
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
