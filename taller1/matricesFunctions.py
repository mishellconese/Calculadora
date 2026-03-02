import numpy as np

class OperacionesMatrices:
    def __init__(self, A, B=None, v=None):
        self.A=np.array(A, dtype=float)
        self.B=None if B is None else np.array(B, dtype=float)
        self.v=None if v is None else np.array(v, dtype=float)

    def getSuma(self):
        if self.B is None:
            raise Exception("Error: Para sumar se necesita la matriz B.")
        if self.A.shape!=self.B.shape:
            raise Exception("Error: A y B deben tener las mismas dimensiones para sumar.")
        return self.A+self.B

    def getProducto(self):
        if self.B is None:
            raise Exception("Error: Para multiplicar se necesita la matriz B.")
        if self.A.shape[1]!=self.B.shape[0]:
            raise Exception("Error: Columnas(A) debe ser igual a filas(B).")
        return self.A@self.B

    def getInversa(self):
        if self.A.shape[0]!=self.A.shape[1]:
            raise Exception("Error: La inversa solo existe para matrices cuadradas.")
        det = np.linalg.det(self.A)
        if abs(det)<1e-12:
            raise Exception("Error: La matriz no es invertible (determinante = 0).")
        return np.linalg.inv(self.A)

    def getMatrizVector(self):
        if self.v is None:
            raise Exception("Error: Para Matriz x Vector se necesita el vector v.")
        if self.A.shape[1]!=self.v.shape[0]:
            raise Exception("Error: Tamaño(v) debe ser igual a columnas(A).")
        return self.A@self.v