from basicas import OpBasicas
from avanzadas import OpAvanzadas
from trigonometricas import OpTrigonometricas

def menu():
    print("\nCALCULADORA\n")
    print(f"{'1 Suma':<20}{'8 Potencia'}")
    print(f"{'2 Resta':<20}{'9 Raiz'}")
    print(f"{'3 Multiplicacion':<20}{'10 Factorial'}")
    print(f"{'4 Division':<20}{'11 Fibonacci'}")
    print(f"{'5 Seno':<20}{'12 MCD'}")
    print(f"{'6 Coseno':<20}{'13 MCM'}")
    print(f"{'7 Tangente':<20}{'14 IVA'}")
    print("\n0 SALIR DEL MENU")

def main():
    bas=OpBasicas()
    av=OpAvanzadas()
    tri=OpTrigonometricas()

    print("CALCULADORA")
    while True:
        try:
            res=float(input("VALOR PARA INCIAR: "))
            break
        except:
            print("ERROR: debe ingresar un numero")

    while True:
        print("Acumulado: ",res)
        menu()
        try:
            op=int(input("Eliga una de las opciones del menu: "))
        except:
            print("Opcion no valida, debe ser un numero")
            continue
        if op==0:
            break
        elif op in [1,2,3,4,8]:
            v=float(input("Ingrese valor: "))
            if op==1:
                res=bas.suma(res,v)
            elif op==2:
                res=bas.resta(res,v)
            elif op==3:
                res=bas.multiplicacion(res,v)
            elif op==4:
                res=bas.division(res,v)
            elif op==8: 
                res=av.potenciaenesima(res,v)
            print("Resultado: ",res)
        elif op==5:
            ang=float(input("Ingrese el ángulo: "))
            print("Resultado:", tri.seno(ang))

        elif op==6:
            ang=float(input("Ingrese el ángulo: "))
            print("Resultado:", tri.coseno(ang))

        elif op==7:
            ang=float(input("Ingrese el ángulo: "))             
            print("Resultado:", tri.tangente(ang))

        elif op==9:
            num=float(input("Ingrese el número: "))
            ind=int(input("Ingrese el índice: "))
            print("Resultado:", av.raizenesima(num, ind))

        elif op==10:
            n=int(input("Ingrese un entero: "))
            print("Resultado:", av.factorial(n))

        elif op==11:
            n=int(input("Ingrese n: "))
            print("Resultado:", av.fibonacci(n))

        elif op==12:
            a=int(input("Ingrese a: "))
            b=int(input("Ingrese b: "))
            print("Resultado:", av.mcd(a, b))

        elif op==13:
            a=int(input("Ingrese a: "))
            b=int(input("Ingrese b: "))
            print("Resultado:", av.mcm(a, b))

        elif op==14:
            val=float(input("Ingrese el valor: "))
            porc=float(input("Ingrese el IVA %: "))
            iva, total=av.iva(val, porc)               
            print("IVA:", iva)
            print("Total:", total)
        else:
            print("Opcion no válida")
#ejecucion
main()