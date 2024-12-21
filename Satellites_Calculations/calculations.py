import math as ma

class Himmelskoerper:

    G = 6.67428e-11          #Gravitationskonstante  ((N * m ** 2) / kg **2)
    deltaTime = 60           # 1 Minute pro Frame

    def __init__(self, x, y, masse):
        self.x = x
        self.y = y
        # self.radius = radius // jetzt bei class Visualisierung
        self.masse = masse      # in kg
        # self.farbe = farbe // jetzt bei class Visualisierung
        self.orbit = []
        self.planet = False
        self.x_v = 0    #geschwindigkeit (in x - Richtung)
        self.y_v = 0    #geschwindigkeit (in y - Richtung)


class BewegenderHimmelskoerper(Himmelskoerper):

    def anziehung(self, other):     #Static?        resolved: Nein

        other_x = other.x
        other_y = other.y

        distance_x = other_x - self.x
        distance_y = other_y - self.y

        distance_generell = ma.sqrt(distance_x ** 2 + distance_y ** 2)


        if distance_generell == 0:
            f_generell = 0

            # ab hier eigentlich unnötig, da fy und fx sowieso = 0 sind, aber für Verständlichkeit // UND: dass eventuell kein Fehler bei distance = 0 kommt, da fx und fy = undefined
            alpha = ma.atan2(distance_y, distance_x)

            fy = ma.sin(alpha) * f_generell

            fx = ma.cos(alpha) * f_generell

        else:
            f_generell = (self.G * self.masse * other.masse) / distance_generell ** 2

            alpha = ma.atan2(distance_y, distance_x)

            fy = ma.sin(alpha) * f_generell

            fx = ma.cos(alpha) * f_generell
            #print(alpha * 180 / ma.pi) #debugging fertig
        return fx, fy

    def position_berechnen(self, satelliten):
        f_x_total = f_y_total = 0

        for tupel in satelliten:    # satellit (bzw. "koerper") muss erst aus tupel an Stelle 0 extrahiert werden, sonst versuch tupel mit attribut aufzurufen
            satellit = tupel[0]

            if self.planet is True:     # WARUM?
                continue

            if self != satellit:
                fx, fy = self.anziehung(satellit)
                f_x_total += fx
                f_y_total += fy

        self.x_v = self.x_v + (f_x_total / self.masse) * self.deltaTime      # das Gleiche wie self.x_v += (f_x_total / self.masse) * self.TimeStep aber schöner
        self.y_v = self.y_v + (f_y_total / self.masse) * self.deltaTime

        self.x += self.x_v * self.deltaTime
        self.y += self.y_v * self.deltaTime

        self.orbit.append((self.x, self.y))

