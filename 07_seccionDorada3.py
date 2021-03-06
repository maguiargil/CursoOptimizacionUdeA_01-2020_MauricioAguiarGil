#Instalar la librería tabulate usando pip install tabulate en una ventana del cmd de Windows

import math
from tabulate import tabulate

phi = (math.sqrt(5) - 1) / 2

def function(x):
    fx = 6 * math.cos(x) - 1.5 * math.sin(x)
    #fx = -1.5 * math.pow(x,6) - 2 * math.pow(x,4) + 12 * x
    #fx = 2 * math.sin(x) - math.pow(x, 2) / 10
    return fx

def goldenRatio (xl, xu):

    x_uno = xu - phi * (xu - xl)
    x_dos = xl + phi * (xu - xl)

    fx_uno = function(x_uno)
    fx_dos = function(x_dos)

    return x_uno, x_dos, fx_uno, fx_dos


encabezados = ['iteración', 'xl', 'f(xl)','x2', 'f(x2)','x1', 'f(x1)','xu', 'f(xu)']
tabla = []


min = input("Indicar si desea buscar un mínimo (S/N): ")
while True:
    if min.lower() == 's':
        minimo = True
        busqmax = False
        maximo = False
        break
    elif min.lower() == 'n':
        minimo = False
        busqmax = True
        break
    else:
        input("Indicar si desea buscar un mínimo (S/N): ")


max = input("Indicar si desea buscar un máximo (S/N): ")
while busqmax:
    if max.lower() == 's':
        maximo = True
        break
    elif max.lower() == 'n':
        maximo = False
        break
    else:
        input("Indicar si desea buscar un máximo (S/N): ")


xl = float(input("Indicar límite inferior xl: "))
xu = float(input("Indicar límite superior xu: "))
iteraciones = int(input("Indicar la cantidad de iteraciones deseada para estimar el punto crítico (Número entero positivo): "))


fxl = function(xl)
fxu = function(xu)
x1, x2, fx1, fx2 = goldenRatio(xl, xu)
fila = [1, xl, fxl, x2, fx2, x1, fx1, xu, fxu]
tabla.append(fila)

for iteracion in range(iteraciones - 1):
    if minimo:
        if fx1 > fx2:
            xl = x1
        if fx1 < fx2:
            xu = x2
        fxl = function(xl)
        fxu = function(xu)
        x1, x2, fx1, fx2 = goldenRatio(xl, xu)
        fila = [iteracion + 2, xl, fxl, x2, fx2, x1, fx1, xu, fxu]
        tabla.append(fila)

    if maximo:
        if fx1 > fx2:
            xu = x2
        if fx1 < fx2:
            xl = x1
        fxl = function(xl)
        fxu = function(xu)
        x1, x2, fx1, fx2 = goldenRatio(xl, xu)
        fila = [iteracion + 2, xl, fxl, x2, fx2, x1, fx1, xu, fxu]
        tabla.append(fila)


if minimo:
    if fx1 > fx2:
        xfinal = x2
        print("\n\n")
        print(tabulate(tabla, headers = encabezados))
        print("\n\nSe ha encontrado un mínimo alrededor de (" + str(xfinal) + ", " + str(fx2) + ")")
    if fx1 < fx2:
        xfinal = x1
        print("\n\n")
        print(tabulate(tabla, headers = encabezados))
        print("\n\nSe ha encontrado un mínimo alrededor de (" + str(xfinal) + ", " + str(fx1) + ")")

if maximo:
    if fx1 > fx2:
        xfinal = x1
        print("\n\n")
        print(tabulate(tabla, headers = encabezados))
        print("\n\nSe ha encontrado un máximo alrededor de (" + str(xfinal) + ", " + str(fx1) + ")")
    if fx1 < fx2:
        xfinal = x2
        print("\n\n")
        print(tabulate(tabla, headers = encabezados))
        print("\n\nSe ha encontrado un máximo alrededor de (" + str(xfinal) + ", " + str(fx2) + ")")
