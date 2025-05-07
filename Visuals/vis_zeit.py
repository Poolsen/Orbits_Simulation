import config
from Visuals import vis_draw_text
import datetime

current_date = datetime.datetime(2025, 1, 1, 0, 0)

def vis_ingame_time():

    time_increment = datetime.timedelta(seconds = config.deltaTime)    #da hier deltaTime nur aus config gelesen werden muss, muss sie nicht davor mit global deklariert werden

    global current_date
    current_date = current_date + time_increment
    formatted_current_date = current_date.strftime('%d. %b %Y, %H:%M')

    current_time_text = f"Zeit: {formatted_current_date} Uhr"

    vis_draw_text(current_time_text, config.font_arial, (255, 255, 255), (5, 27),None)






"""
def vis_ingame_time(zeit_min, zeit_h, zeit_tag, monat, zeit_jahr):

    # pro frame werden 60 s abgedeckt --> pro iteration wird 1 min hinzugefügt

    zeit_min += 1

    if zeit_min >= 60:
        zeit_h += 1
        zeit_min = 0
        if zeit_h >= 24:
            zeit_tag += 1
            zeit_h = 0
            if zeit_tag >= 28:
                if monat == "Januar":
                    if zeit_tag >= 31:
                        monat = "Februar"
                        zeit_tag = 1
                elif monat == "Februar":
                    if zeit_tag >= 28:
                        monat = "März"
                        zeit_tag = 1
                elif monat == "März":
                    if zeit_tag >= 31:
                        monat = "April"
                        zeit_tag = 1
                elif monat == "April":
                    if zeit_tag >= 30:
                        monat = "Mai"
                        zeit_tag = 1
                elif monat == "Mai":
                    if zeit_tag >= 31:
                        monat = "Juni"
                        zeit_tag = 1
                elif monat == "Juni":
                    if zeit_tag >= 30:
                        monat = "August"
                        zeit_tag = 1
                elif monat == "August":
                    if zeit_tag >= 31:
                        monat = "September"
                        zeit_tag = 1
                elif monat == "September":
                    if zeit_tag >= 30:
                        monat = "Oktober"
                        zeit_tag = 1
                elif monat == "Oktober":
                    if zeit_tag >= 31:
                        monat = "November"
                        zeit_tag = 1
                elif monat == "November":
                    if zeit_tag >= 30:
                        monat = "Dezember"
                        zeit_tag = 1
                elif monat == "Dezember":
                    if zeit_tag >= 31:
                        monat = "Januar"
                        zeit_tag = 1
                        zeit_jahr += 1
                else:
                    print("Dieser Monat existiert nicht!")



    current_time_text = f"Zeit: {zeit_h} : {zeit_min} Uhr  {zeit_tag}. {monat}  {zeit_jahr}"
    return vis_draw_text(current_time_text, font_arial, (255, 255, 255), (5, 25), None), zeit_min, zeit_h, zeit_tag, monat, zeit_jahr
""" #das war meine eigene Zeit library (: datetime ist besser ):


