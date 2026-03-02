import numpy as np
from matricesFunctions import OperacionesMatrices

def leerentero(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Error: ingresa un numero entero.")

def leerfloat(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Error: ingresa un numero float.")

def leermatriz(nombre):
    f=leerentero("Filas de "+nombre+": ")
    c=leerentero("Columnas de "+nombre+": ")

    print("Ingrese los valores de " + nombre + " (fila por fila):")
    M=[]
    for i in range(f):
        fila=[]
        for j in range(c):
            fila.append(leerfloat(nombre+"["+str(i)+"]["+str(j)+"]: "))
        M.append(fila)

    return np.array(M, dtype=float)

def leervector(nombre, n):
    print("Ingrese los valores del vector "+nombre+":")
    v=[]
    for i in range(n):
        v.append(leerfloat(nombre+"["+str(i)+"]: "))
    return np.array(v, dtype=float)

def imprimirmatriz(M):
    f, c=M.shape
    for i in range(f):
        for j in range(c):
            print(f"{M[i, j]:.2f}", end="   ")
        print()

def imprimirvector(v):
    for i in range(len(v)):
        print(f"{v[i]:.2f}", end="   ")
    print()

def menuprincipal():
    print("\n====== MATRICES ======")
    print("1. Suma de matrices (A + B)")
    print("2. Producto de matrices (A x B)")
    print("3. Inversa de A")
    print("4. Producto matriz por vector (A x v)")
    print("0. Salir")

def submenu():
    print("\n--- Submenu ---")
    print("1. Usar A (acumulado)")
    print("2. Cambiar A (ingresar nueva)")
    print("0. Volver al principal")

def main():
    print("Calculadora con matrices")

    print("Ingrese la matriz inicial A (acumulado):")
    A = leermatriz("A")

    while True:
        print("Matriz A (acumulado):")
        imprimirmatriz(A)

        menuprincipal()
        op=leerentero("Opcion: ")

        if op==0:
            print("Saliendo...")
            break

        if op not in [1, 2, 3, 4]:
            print("Opción no valida.")
            continue

        while True:
            submenu()
            s=leerentero("Subopcion: ")

            if s==0:
                break

            if s==2:
                print("\nIngrese la nueva matriz A:")
                A=leermatriz("A")

            try:
                if op==1:
                    print("SUMA: A + B")
                    B=leermatriz("B")
                    ops=OperacionesMatrices(A, B=B)
                    A=ops.getSuma()
                    print("Resultado (nuevo A):")
                    imprimirmatriz(A)

                elif op==2:
                    print("PRODUCTO: A x B")
                    B=leermatriz("B")
                    ops=OperacionesMatrices(A, B=B)
                    A=ops.getProducto()
                    print("\nResultado (nuevo A):")
                    imprimirmatriz(A)

                elif op==3:
                    print("INVERSA: A^-1")
                    ops = OperacionesMatrices(A)
                    inv = ops.getInversa()
                    print("\nInversa de A:")
                    imprimirmatriz(inv)

                    r=leerentero("¿Reemplazar A por su inversa? (1=si, 0=no): ")
                    if r==1:
                        A=inv
                        print("A actualizado.")

                elif op==4:
                    print("\nMATRIZ x VECTOR: A x v")
                    v=leervector("v", A.shape[1])
                    ops=OperacionesMatrices(A, v=v)
                    res=ops.getMatrizVector()
                    print("Resultado (vector):")
                    imprimirvector(res)

            except Exception as e:
                print(e)

            break

if __name__ == "__main__":
    main()