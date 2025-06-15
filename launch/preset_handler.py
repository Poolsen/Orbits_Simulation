import os
import sys
import json
import config


def create_preset_data_json():
    try:
        with open(config.PRESET_FILE, "w") as file:
            json_object: dict = {
                "Comment": "This file saves all presets. Please do not touch (;",
                "number_of_presets": 0,
                "size ()": "",
                "Presets": {}
            }
            json_object["size ()"] = f"{sys.getsizeof(json_object)} Bytes"
            json.dump(json_object,
                      fp=file, # type: ignore
                      indent = 6)

    except Exception as e:
        raise Exception(f"Es passierte der folgende kritische Fehler: {e}")

def add_preset_data():
    if os.path.exists(config.PRESET_FILE):
        pass
    else:
        create_preset_data_json()
        print(config.Colors.WARNING + "WARNING: THE FILE YOU TRIED TO ACCESS DOES NOT EXIST. A NEW FILE HAS BEEN CREATED" + config.Colors.ENDC)

    with (open(config.PRESET_FILE, "r+") as file):
        json_object = json.load(file)

        all_args: dict = {}
        configuring_presets = True

        while configuring_presets:
            preset_name = input("Name des Presets: ").strip()

            n = 1
            weiteres_objekt = True

            while weiteres_objekt:
                mass = input("Masse [kg]: ").strip()
                x = input("X-Koordinate [m]: ").strip()
                y = input("Y-Koordinate [m]: ").strip()
                y_v = input("Startgeschwindigkeit nach unten [m/s]: ").strip()
                x_v = input("Startgeschwindigkeit nach rechts [m/s]: ").strip()

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
                            "").strip():
                    case "n" | "N" | "m" | "M":
                        weiteres_objekt = False

                    case _:
                        pass

            match input("Presets erstellen: \n"
                        "Save und Weiter (' ') \n"
                        "Save und Quit ('q') \n"
                        "Exit ohne Speichern ('e') \n"
                        "Weiter ohne Speichern ('c') \n").strip():

                #save and continue
                case "":
                    json_object["Presets"][f"{preset_name}"] = all_args
                    json_object["number_of_presets"] =int(
                        json_object.get("number_of_presets")) + 1

                    file.seek(0, 0)
                    file.truncate()

                    json.dump(json_object,
                              file, # type: ignore
                              indent=6)
                    file.flush()

                    json_object["size ()"] = f"{os.path.getsize(config.PRESET_FILE)} Bytes"

                    file.seek(0, 0)
                    file.truncate()
                    json.dump(json_object,
                              file, # type: ignore
                              indent=6)

                    all_args = {}
                    configuring_presets = True


                #quit, save and exit
                case "q":
                    json_object["Presets"][f"{preset_name}"] = all_args
                    json_object["number_of_presets"] = int(json_object.get("number_of_presets")) + 1

                    file.seek(0, 0)
                    file.truncate()

                    json.dump(json_object,
                              file, # type: ignore
                              indent=6)
                    file.flush()

                    json_object["size ()"] = f"{os.path.getsize(config.PRESET_FILE)} Bytes"

                    file.seek(0, 0)
                    file.truncate()
                    json.dump(json_object,
                              file, # type: ignore
                              indent=6)

                    all_args = {}
                    configuring_presets = False

                #exit ohne Speichern
                case "e":
                    all_args = {}
                    configuring_presets = False

                #continue ohne Speichern
                case "c":
                    all_args = {}
                    configuring_presets = True

                #rest = save and continue
                case _:
                    json_object["Presets"][f"{preset_name}"] = all_args
                    json_object["number_of_presets"] = int(int(json_object.get("number_of_presets")) + 1)

                    file.seek(0, 0)
                    file.truncate()

                    json.dump(json_object,
                              file, # type: ignore
                              indent=6)
                    file.flush()

                    json_object["size ()"] = f"{os.path.getsize(config.PRESET_FILE)} Bytes"

                    file.seek(0, 0)
                    file.truncate()
                    json.dump(json_object,
                              file, # type: ignore
                              indent=6)

                    all_args = {}
                    configuring_presets = True


        del json_object


def read_preset_data():
    if not os.path.exists(config.PRESET_FILE):
        print(config.Colors.ERROR + "ERROR: THE FILE YOU TRIED TO ACCESS DOES NOT EXIST!" + config.Colors.ENDC)
        if input(config.Colors.ERROR + "DO YOU WANT TO CREATE THE FILE? (y/n) \n" + config.Colors.ENDC).strip() == "y":
            create_preset_data_json()
        else:
            return None

    with open(config.PRESET_FILE) as file:
        data = json.load(file)
        all_presets_list: list = list(data["Presets"].keys())

        if len(all_presets_list) > 0:
            pass
        else:
            if input(config.Colors.WARNING + "Es scheint kein Preset im File zu existieren.\n"
                                            "Das Directory konnte aber gefunden werden. \n"
                                            "Preset hinzufügen und später erneut versuchen? (y/n) \n" + config.Colors.ENDC).strip() == "y":
                add_preset_data()
            else:
                pass

            return None


        #preset_matcher_int: dict = {}
        #preset_matcher_string: list = []

        print("Gespeicherte Presets:")

        #for preset_position in range(len(all_presets_list)):
            #print(f"(Preset {preset_position + 1}): {all_presets_list[preset_position]}")
            #preset_matcher_int[f"{preset_position + 1}"] = f"{all_presets_list[preset_position]}"
            #preset_matcher_string.append(f"{all_presets_list[preset_position]}")

        for preset in all_presets_list:
            print(f"(Preset {int(all_presets_list.index(str(preset))) + 1}): {preset}")

        decision = False
        while not decision:
            select = input("Welches der Presets soll geladen werden?\n").strip()

            if select.strip().isdigit():
                index = int(select) - 1
                if 0 <= index < len(all_presets_list):
                    chosen = all_presets_list[index]
            elif select in all_presets_list:
                chosen = select
            else:
                print(config.Colors.WARNING + "Ungültige Auswahl." + config.Colors.ENDC)
                continue

            if input(f"Soll Preset '{chosen}' geladen werden? (y/n)\n").strip().lower() == "y":
                decision = True
            else:
                pass

        return object_creation(data, chosen)

def object_creation(data, chosen):
    from Satellites_Calculations import MovingObject
    from Visuals import Visualisierung

    moving_objects: list = []
    preset: dict = data["Presets"][f"{chosen}"]

    for n in range(len(preset)):
        new_moving_object = MovingObject(preset[f"object no.: {n+1}"].get("x"),
                                         preset[f"object no.: {n+1}"].get("y"),
                                         preset[f"object no.: {n+1}"].get("mass"))

        new_moving_object.x_v = preset[f"object no.: {n+1}"].get("x_v")
        new_moving_object.y_v = preset[f"object no.: {n+1}"].get("y_v")

        if preset[f"object no.: {n + 1}"]["id"] == 0:  # Zentral-Teil
            new_visual_object = Visualisierung(config.hellblau, 30)

        else:
            new_visual_object = Visualisierung(config.weiss, 20)

        moving_objects.append((new_moving_object, new_visual_object))  # klammer wichtig, um als tuple zu passen
        return moving_objects



""" Alte Methode zum Akzeptieren von ints UND strings als Input für die Auswahl 
        try:
            select = int(select)
        except ValueError:
            pass

        if type(select) == int:
            input(f"Soll Preset '{preset_matcher_int[str(select)]}' geladen werden? (y/n)\n")

        elif type(select) == str:
            if select in preset_matcher_string:
                select_int_position: int = preset_matcher_string.index(f"{select}") + 1
                input(f"Soll Preset '{preset_matcher_int[str(select_int_position)]}' geladen werden? (y/n)\n")

        print(preset_matcher_int)
        print(preset_matcher_string)
        del preset_matcher_int, preset_matcher_string
"""


def delete_preset_data():
    if os.path.exists(config.PRESET_FILE):
        os.remove(config.PRESET_FILE)
    else:
        print("The file does not exist")
