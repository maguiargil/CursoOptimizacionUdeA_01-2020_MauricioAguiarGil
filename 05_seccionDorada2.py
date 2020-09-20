#Instalar la librería tabulate usando pip install tabulate en una ventana del cmd de Windows

import math
from tabulate import tabulate

phi = (math.sqrt(5) - 1) / 2

def function(x):
    fx = -0.3 * math.pow(x,4) + 1.2 * math.pow(x,3) - 1.8 * math.pow(x,2) + 4 * x
    return fx

def goldenRatio (xl, xu):

    x_uno = xu - phi * (xu - xl)
    x_dos = xl + phi * (xu - xl)

    fx_uno = function(x_uno)
    fx_dos = function(x_dos)

    return x_uno, x_dos, fx_uno, fx_dos

def tolerance(x_may, tol):
    if 100 * (abs(x_may - 2.32635) / 2.32635) <=  tol:
        return False
    else:
        return True

def porc_error(x_may):
    err =  (100 * (abs(x_may - 2.32635) / 2.32635))
    return err


encabezados = ['xl', 'f(xl)','x2', 'f(x2)','x1', 'f(x1)','xu', 'f(xu)', '% error']
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
toler = float(input("Indicar el porcentaje de error deseado: "))

abs1 = abs(xl - 2.32635)
abs2 = abs(xu - 2.32635)
if abs1 < abs2:
    tolerancia = tolerance(xl, toler)
    errhor = '{:.2f}%'.format(porc_error(xl))
else:
    tolerancia = tolerance(xu, toler)
    errhor = '{:.2f}%'.format(porc_error(xu))

fxl = function(xl)
fxu = function(xu)
x1, x2, fx1, fx2 = goldenRatio(xl, xu)
fila = [xl, fxl, x2, fx2, x1, fx1, xu, fxu, errhor]
tabla.append(fila)

while tolerancia:
    if minimo:
        if fx1 > fx2:
            xl = x1
        if fx1 < fx2:
            xu = x2
        fxl = function(xl)
        fxu = function(xu)
        x1, x2, fx1, fx2 = goldenRatio(xl, xu)

    if maximo:
        if fx1 > fx2:
            xu = x2
        if fx1 < fx2:
            xl = x1
        fxl = function(xl)
        fxu = function(xu)
        x1, x2, fx1, fx2 = goldenRatio(xl, xu)


    abs1 = abs(xl - 2.32635)
    abs2 = abs(xu - 2.32635)
    if abs1 < abs2:
        tolerancia = tolerance(xl, toler)
        errhor = '{:.2f}%'.format(porc_error(xl))
    else:
        tolerancia = tolerance(xu, toler)
        errhor = '{:.2f}%'.format(porc_error(xu))

    fila = [xl, fxl, x2, fx2, x1, fx1, xu, fxu, errhor]
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
