#SERIE tres numeros de inicio (1,2,3)

def serie(posicion):
    if posicion==1: print("el numero de la serie es:", 1)
    if posicion==2: print("el numero de la serie es:", 2)
    if posicion==3: print("el numero de la serie es:", 3)   
    elif posicion>=4:
        a,b,c=1,2,3
        d=a+b+c
        i=4 
        while i<=posicion:
            d=a+b+c
            a=b
            b=c
            c=d
            i+=1
        print("el numero de la serie es:", d)
        
        
#hacer guia 1 con funciones 