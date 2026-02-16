class OpBasicas:
    def suma(self,a,b):
        return a+b
    def resta(self,a,b):
        return a-b
    def multiplicacion(self, a,b):
        return a*b
    def division(self,a,b):
        if b!=0:
            return round(a/b,3)
        else:
            return "Error: Division por cero"