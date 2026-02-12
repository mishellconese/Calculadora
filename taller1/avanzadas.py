def potenciaenesima(base, exponente):
    return base ** exponente

def raizenesima(numero, indice):
    if indice == 0:
        return "Indice no valido"
    if numero < 0 and indice % 2 == 0:
        return "Resultado imaginario"
    return round(numero ** (1 / indice), 3)

def factorial(n):
    if n < 0:
        return "Error: número negativo"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fibonacci(n):
    if n <= 0:
        return "Error: n debe ser mayor que 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

def calculariva(valor, porcentaje):
    iva = valor * porcentaje / 100
    total = valor + iva
    return iva, total
