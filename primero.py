"""a=int(input("Enter first number: "))
if a==2:
    print("ingreso el numero correcto")
    print("estoy dentro del if")
    if nombre=="ana":
        print("esta autorizado para ejecutar el programa")
    else:
        print("no esta autorizado para ejecutar el programa")
elif a==3:
    print("ingreso el numero 3")
    print("estoy dentro del elif3")
elif a==4:
    print("ingreso el numero 4")
    print("estoy dentro del elif4")
elif a==6 and nombre=="juan":
    print("esta autorizado")

else:
    print("ingreso a una opcion  incorrecto")
    print("estoy dentro del else")
print("fin del programa") """
"""
#ejemplo del FOR (solo de tipo enterto INT)

sup=int(input("ingrese el numero superior: "))
for i in range (1, sup+1, 1): #condicion de que llegue a un numero mas que el requerido
    print (i, end=" ")
    print("estoy dentro del for")
print("fin del ciclo for")
    
    
#ejemplo del WHILE
i=1
while i<=sup:
    if i==3:
        i+=1
        continue #rompe el ciclo del while, no cuenta el 3
    print(i, end=" ")
    print("estoy dentro del while")
    i+=1
    """
    
def suma(a, b):
        return a+b, a-b, a*b, a/b

c=int(input("ingrese un numero: ") )
d=int(input("ingrese un numero: ") )
#resultado=suma(c, d)
print("el resultado de la suma es: ", suma(c,d))#(resultado)
        