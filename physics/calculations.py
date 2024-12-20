import math as ma

class Satellit:
    AE = 149600000 * 1000   #149,6 Millionen km, aber in metern also * 1000
    G = 6.67428e-11         #Gravitationskonstante  ((N * m ** 2) / kg **2)
    Scale = 1 / 1e5         # 1 Pixel = 100.000 m = 100 km
    deltaTime = 60           # 1 Minute pro Frame

    def __init__(self, x, y, radius, masse, farbe):
        self.x = x
        self.y = y

        self.radius = radius
        self.masse = masse      # in kg
        self.farbe = farbe

        self.orbit = []
        self.planet = False
        self.abstand_zu_Planet = 0

        self.x_v = 0    #geschwindigkeit (in x - Richtung)
        self.y_v = 0    #geschwindigkeit (in y - Richtung)

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

    def postion_berechnen(self, satelliten):
        f_x_total = f_y_total = 0

        for satellit in satelliten:

            if self.planet is True:
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
