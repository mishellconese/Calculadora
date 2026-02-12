from basicas import *
from trigonometricas import *
from avanzadas import *

def menu():
    print("\n        CALCULADORA\n")

    print(f"{'1 Suma':<20}{'8 Potencia'}")
    print(f"{'2 Resta':<20}{'9 Raíz'}")
    print(f"{'3 Multiplicación':<20}{'10 Factorial'}")
    print(f"{'4 División':<20}{'11 Fibonacci'}")
    print(f"{'5 Seno':<20}{'12 MCD'}")
    print(f"{'6 Coseno':<20}{'13 MCM'}")
    print(f"{'7 Tangente':<20}{'14 IVA'}")

    print("\n0 Salir")


def main():
    print("Calculadora")

    while True:
        try:
            res = float(input("Valor inicial: "))
            break
        except ValueError:
            print("Error: número inválido")

    while True:
        print("Acumulado:", res)
        menu()

        try:
            op = int(input("Opción: "))
        except ValueError:
            print("Error: opción inválida")
            continue

        if op == 0:
            print("Saliendo...")
            break

        elif op == 1:
            v = float(input("Ingrese valor: "))
            res = sumar(res, v)
            print("Resultado:", res)

        elif op == 2:
            v = float(input("Ingrese valor: "))
            res = restar(res, v)
            print("Resultado:", res)

        elif op == 3:
            v = float(input("Ingrese valor: "))
            res = multiplicar(res, v)
            print("Resultado:", res)

        elif op == 4:
            v = float(input("Ingrese valor: "))
            res = dividir(res, v)
            print("Resultado:", res)

        elif op == 5:
            ang = float(input("Ingrese el ángulo: "))
            print("Resultado:", seno(ang))

        elif op == 6:
            ang = float(input("Ingrese el ángulo: "))
            print("Resultado:", coseno(ang))

        elif op == 7:
            ang = float(input("Ingrese el ángulo: "))
            print("Resultado:", tangente(ang))

        elif op == 8:
            v = float(input("Ingrese exponente: "))
            res = potenciaenesima(res, v)
            print("Resultado:", res)

        elif op == 9:
            num = float(input("Ingrese el número: "))
            ind = int(input("Ingrese el índice: "))
            print("Resultado:", raizenesima(num, ind))

        elif op == 10:
            n = int(input("Ingrese un entero: "))
            print("Resultado:", factorial(n))

        elif op == 11:
            n = int(input("Ingrese n: "))
            print("Resultado:", fibonacci(n))

        elif op == 12:
            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))
            print("Resultado:", mcd(a, b))

        elif op == 13:
            a = int(input("Ingrese a: "))
            b = int(input("Ingrese b: "))
            print("Resultado:", mcm(a, b))

        elif op == 14:
            val = float(input("Ingrese el valor: "))
            porc = float(input("Ingrese el IVA %: "))
            iva, total = calculariva(val, porc)
            print("IVA:", iva)
            print("Total:", total)

        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
