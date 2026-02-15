class OpAvanzadas:
    def potenciaenesima(self,base,exponente):
        return base**exponente
    def raizenesima(self,numero,indice):
        if indice==0:
            return "Indice invalido"
        if numero<0 and indice%2==0:
            return "Resultado imaginario"
        return round(numero**(1/indice),3)
    def factorial(self,n):
        if n<0:
            return "Error: el numero debe ser positivo"
        resultado=1
        for i in range(1,n+1):
            resultado*=i
        return resultado
    def fibonacci(self,n):
        if n<=0:
            return "Error: el numero no puede ser 0"
        if n==1:
            return 0
        elif n==2:
            return 1
        return self.fibonacci(n-1)+self.fibonacci(n-2)
    def mcd(self,a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def mcm(self,a,b):
        return abs(a*b)//self.mcd(a,b)
    def iva(self,valor,porcentaje):
        iva=valor*porcentaje/100
        total=valor+iva
        return iva,total