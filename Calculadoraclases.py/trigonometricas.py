import math
class OpTrigonometricas:
    def __init__(self):
        self.nombre = "Operaciones Trigonométricas"
    def seno(self,angulo):
        return math.sin(math.radians(angulo))

    def coseno(self,angulo):
        return math.cos(math.radians(angulo))

    def tangente(self,angulo):
        if angulo % 180 == 90:
            return "Error: tangente indefinida"
        return math.tan(math.radians(angulo))
