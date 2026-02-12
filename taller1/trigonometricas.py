import math

def seno(angulo):
    return math.sin(math.radians(angulo))

def coseno(angulo):
    return math.cos(math.radians(angulo))

def tangente(angulo):
    if angulo % 180 == 90:
        return "Error: tangente indefinida"
    return math.tan(math.radians(angulo))
