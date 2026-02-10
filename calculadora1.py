import math

#operaciones b
def sumar(a, b):
    return a+b

def restar(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    if b!=0:
        return round(a/b, 3)
    else:
        return "Error: división por cero"

#trigonometricas
def seno(angulo):
    return math.sin(math.radians(angulo))   

def coseno(angulo):
    return math.cos(math.radians(angulo))   

def tangente(angulo):
    if angulo%180==90:
        return "Error: tangente indefinida"
    return math.tan(math.radians(angulo))

#potencias y raices
def potenciaenesima(base, exponente):
    return base**exponente

def raizenesima(numero, indice):
    if indice==0:
        return"Indice no valido"
    if numero<0 and indice%2==0:
        return "Resultado imaginario"
    return round (numero**(1/indice), 3)

#factorial 
def factorial(n):
    if n<0:
        return "Error: número negativo"
    resultado=1
    for i in range(1, n + 1):
        resultado*=i
    return resultado

#fibonacci 
def fibonacci(n):
    if n<=0:
        return "Error: n debe ser mayor que 0"
    elif n==1:
        return 0
    elif n==2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b=b, a+b
    return b

#MCD Y MCM 
def mcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def mcm(a, b):
    return abs(a*b)//mcd(a, b)

#IVA
def calculariva(valor, porcentaje):
    iva=valor*porcentaje/100
    total=valor+iva
    return iva, total


#menu
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



#programa 
def main():
    print("Calculadora")
    while True:
        try:
            res=float(input("Valor inicial: "))
            break
        except ValueError:
            print("Error: número inválido")

    while True:
        print("Acumulado:",res)
        menu()
        try:
            op=int(input("Opción: "))
        except ValueError:
            print("Error: opción inválida")
            continue

        if op==0:
            print("Saliendo...")
            break

        elif op in [1,2,3,4,8]:
            v=float(input("Ingrese valor: "))
            if op==1:
                res=sumar(res,v)
            elif op==2:
                res=restar(res,v)
            elif op==3:
                res=multiplicar(res,v)
            elif op==4:
                res=dividir(res,v)
            elif op==8: 
                res=potenciaenesima(res,v)
            print("Resultado: ",res)

        elif op==5:
            ang=float(input("Ingrese el ángulo: "))
            resultado=seno(ang)
            
            print("Resultado:", seno(ang))

        elif op==6:
            ang=float(input("Ingrese el ángulo: "))
            resultado=coseno(ang)
            print("Resultado:", coseno(ang))

        elif op==7:
            ang=float(input("Ingrese el ángulo: "))
            res=tangente(ang) 

            if isinstance(res, str):
                print (res)
            else:
                resultado=res              
            print("Resultado:", tangente(ang))

        elif op==9:
            num=float(input("Ingrese el número: "))
            ind=int(input("Ingrese el índice: "))
            res=raizenesima(num, ind)

            if isinstance(res, str):
                print(res)
            else:
                resultado=res
            print("Resultado:", raizenesima(num, ind))

        elif op==10:
            n=int(input("Ingrese un entero: "))
            res=factorial(n)

            if isinstance(res, str):
                print(res)
            else:
                resultado=res
            print("Resultado:", factorial(n))

        elif op==11:
            n=int(input("Ingrese n: "))
            res=fibonacci(n)

            if isinstance(res, str):
                print(res)      
            else:
                resultado=res
            print("Resultado:", fibonacci(n))

        elif op==12:
            a=int(input("Ingrese a: "))
            b=int(input("Ingrese b: "))
            resultado=mcd(a, b)
            print("Resultado:", mcd(a, b))

        elif op==13:
            a=int(input("Ingrese a: "))
            b=int(input("Ingrese b: "))
            resultado=mcm(a, b)   
            print("Resultado:", mcm(a, b))

        elif op==14:
            val=float(input("Ingrese el valor: "))
            porc=float(input("Ingrese el IVA %: "))
            iva, total=calculariva(val, porc)
            resultado=total               
            print("IVA:", iva)
            print("Total:", total)

        else:
            print("Opcion no válida")

#ejecucion
main()


