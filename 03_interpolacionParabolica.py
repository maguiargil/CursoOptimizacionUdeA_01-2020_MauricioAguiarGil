#Instalar la librería tabulate usando pip install tabulate en una ventana del cmd de Windows

import math
from tabulate import tabulate

def funcion(x):
    fx = -1.5 * math.pow(x,6) - 2 * math.pow(x,4) + 12 * x
    #fx = 2 * math.sin(x) - math.pow(x, 2) / 10
    return fx


x0 = float(input("Indicar x0: "))
x1 = float(input("Indicar x1: "))
x2 = float(input("Indicar x2: "))
precision = int(input("Indicar iteraciones: "))

encabezados = ['x0', 'f(x0)','x1', 'f(x1)','x2', 'f(x2)','x3', 'f(x3)']
tabla = []


def punto_x3(x0, x1, x2):
    fx0 = funcion(x0)
    fx1 = funcion(x1)
    fx2 = funcion(x2)

    termino1 = math.pow(x1,2) - math.pow(x2,2)
    termino2 = math.pow(x2,2) - math.pow(x0,2)
    termino3 = math.pow(x0,2) - math.pow(x1,2)
    termino4 = x1 - x2
    termino5 = x2 - x0
    termino6 = x0 - x1

    x3 = (fx0 * termino1 + fx1 * termino2 + fx2 * termino3) / (2 * (fx0 * termino4 + fx1 * termino5 + fx2 * termino6))
    fx3 = funcion(x3)
    fila = [x0, fx0, x1, fx1, x2, fx2, x3, fx3]
    tabla.append(fila)
    return x3, fx3, fx1

def tipo_extremo(x0, x1, x2):
    fx0 = funcion(x0)
    fx1 = funcion(x1)
    fx2 = funcion(x2)

    num1 = fx0 * (x2 - x1)
    num2 = fx1 * (x2 - x0)
    num3 = fx2 * (x1 - x0)

    num = num1 - num2 + num3

    den1 = x2 - x1
    den2 = x1 * x2 + math.pow(x0,2)
    den3 = x0 * (x2 + x1)

    den = den1 * (den2 - den3)

    b = num / den

    if b > 0:
        tipo = "mínimo"
    elif b < 0:
        tipo = "máximo"
    return tipo


x3, fx3, fx1 = punto_x3(x0, x1, x2)

for iteracion in range(precision):
    if fx3 > fx1:
        x0 = x1
        x1 = x3
        iteracion = iteracion + 1
        x3, fx3, fx1 = punto_x3(x0, x1, x2)
    if fx3 < fx1:
        x2 = x3
        iteracion = iteracion + 1
        x3, fx3, fx1 = punto_x3(x0, x1, x2)

tipoextremo = tipo_extremo(x0, x1, x2)


print("\n\n")
print(tabulate(tabla, headers = encabezados))
print("\n\nSe ha estimado un " + tipoextremo + " alrededor de (" + str(x3) + ", " + str(fx3) + ")")
