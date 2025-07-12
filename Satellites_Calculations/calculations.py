from ctypes import c_double, byref

import config
from Satellites_Calculations import gravitation_interface
from datetime import datetime

class MovingObject:
    G = 6.67428e-11          #Gravitationskonstante  ((N * m ** 2) / kg **2)
    #deltaTime = 60           # 1 Minute pro Frame wird "berechnet" in config
    seconds_per_orbit_point = 60 # jede 60 Sekunden simulationszeit wird ein neuer Punkt in self.orbit hinzugefügt, 60 sekunden ist aus Tests ein guter Kompromiss zwischen leistung und auflösung

    def __init__(self, x, y, masse):
        self.x = x
        self.y = y
        # self.radius = radius // jetzt bei class Visualisierung
        self.masse = masse      # in kg
        # self.farbe = farbe // jetzt bei class Visualisierung
        self.orbit = []
        self.last_orbit_save = datetime(2025, 1, 1, 0, 0)
        self.planet = False
        self.x_v = 0    #geschwindigkeit (in x - Richtung)
        self.y_v = 0    #geschwindigkeit (in y - Richtung)

    def anziehung(self, other):     #Static?        resolved: Nein

        """other_x = other.x
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
        return fx, fy"""

    @staticmethod
    def position_berechnen(satelliten, sim_time):
        """f_x_total = f_y_total = 0

        for tupel in satelliten:    # satellit (bzw. "koerper") muss erst aus tupel an Stelle 0 extrahiert werden, sonst versuch tupel mit attribut aufzurufen (danach ist der Visual-Körper)
            satellit = tupel[0]

            #if self.planet is True:     # WARUM?
            #    continue

            if self != satellit:
                fx, fy = self.anziehung(satellit)
                f_x_total += fx
                f_y_total += fy

        self.x_v = self.x_v + (f_x_total / self.masse) * config.deltaTime      # das Gleiche wie self.x_v += (f_x_total / self.masse) * self.TimeStep aber schöner
        self.y_v = self.y_v + (f_y_total / self.masse) * config.deltaTime

        self.x += self.x_v * config.deltaTime
        self.y += self.y_v * config.deltaTime"""

        # Shared Library
        gravitation_interface.lib.init_objects(len(satelliten), config.deltaTime)

        for tupel in satelliten:
            moving_object = tupel[0]
            gravitation_interface.lib.import_objects(
                moving_object.x,
                moving_object.y,
                moving_object.x_v,
                moving_object.y_v,
                moving_object.masse,
                moving_object.planet
            )

        gravitation_interface.lib.position_calculator(config.deltaTime)

        for n in range(len(satelliten)):
            moving_object = satelliten[n][0]

            x = c_double()
            y = c_double()
            x_v = c_double()
            y_v = c_double()

            gravitation_interface.lib.export_objects(
                n,
                byref(x),
                byref(y),
                byref(x_v),
                byref(y_v),
            )

            moving_object.x = x.value
            moving_object.y = y.value
            moving_object.x_v = x_v.value
            moving_object.y_v = y_v.value

            if (sim_time - moving_object.last_orbit_save).total_seconds() >= MovingObject.seconds_per_orbit_point:      # nur wenn genug Zeit vergangen ist, wird der punkt hinzugefügt
                moving_object.orbit.append((moving_object.x, moving_object.y))
                moving_object.last_orbit_save = sim_time
