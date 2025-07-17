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
                erde_vis = Visualisierung(config.hellblau, 20)

                s1 = MovingObject(-42164 * 1000, 0, 1000)
                s1.y_v = 3.1 * 1000  # 3.1 km/s --> 3100 m/s
                s1_vis = Visualisierung(config.weiss, 8)

                moving_objects.append((erde, erde_vis))
                moving_objects.append((s1, s1_vis))

                do_else = False

            case "gfs":
                from Satellites_Calculations import MovingObject
                from Visuals import Visualisierung

                erde = MovingObject(0, 0, 5.972 * 10 ** 24)
                erde.planet = True
                erde_vis = Visualisierung(config.hellblau, 20)
                moving_objects.append((erde, erde_vis))

                geo = MovingObject(-42164 * 1000, 0, 1000)  #geo höhe
                geo.y_v = 3.0746 * 1000  # 3.1 km/s --> 3100 m/s
                geo_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((geo, geo_vis))

                leo = MovingObject(-7378 * 1000, 0, 1000)   #1km höhe
                leo.y_v = 7.345 * 1000
                leo_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((leo, leo_vis))

                meo = MovingObject(-26378 * 1000, 0, 1000) #20,000 km höhe
                meo.y_v = 3.888 * 1000
                meo_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((meo, meo_vis))

                molniya = MovingObject(-6971 * 1000, 0, 1000) #startet unter der erde
                molniya.y_v = 9.966 * 1000  #startet nach rechts
                molniya_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((molniya, molniya_vis))

                do_else = False

            case "gfs_helio":
                from Satellites_Calculations import MovingObject
                from Visuals import Visualisierung

                sonne = MovingObject(0, 0, 1.989 * 10 ** 30)
                sonne.planet = True
                sonne_vis = Visualisierung(config.gelb, 20)
                moving_objects.append((sonne, sonne_vis))

                erde = MovingObject(-149.6e9, 0, 5.972 * 10 ** 24)
                erde.planet = False
                erde.y_v = 29.78 * 1000
                erde_vis = Visualisierung(config.hellblau, 18)
                moving_objects.append((erde, erde_vis))

                geo = MovingObject(erde.x + -42164 * 1000, 0, 1000)  # geo höhe
                geo.y_v = erde.y_v + 3.0746 * 1000  # 3.1 km/s --> 3100 m/s
                geo_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((geo, geo_vis))

                leo = MovingObject(erde.x + -7378 * 1000, 0, 1000)  # 1km höhe
                leo.y_v = erde.y_v +  7.345 * 1000
                leo_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((leo, leo_vis))

                meo = MovingObject(erde.x + -26378 * 1000, 0, 1000)  # 20,000 km höhe
                meo.y_v = erde.y_v +  3.888 * 1000
                meo_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((meo, meo_vis))

                molniya = MovingObject(erde.x + -6971 * 1000, 0, 1000)  # startet unter der erde
                molniya.y_v = erde.y_v +  9.966 * 1000
                molniya_vis = Visualisierung(config.weiss, 8)
                moving_objects.append((molniya, molniya_vis))

                config.scale_divis = 1e8
                config.deltaTime *= 60
                config.TIME_PER_SIM_SECOND *= 60

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
