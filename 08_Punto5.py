#Instalar la librería SYMPY digitando en una consola de Windows: pip install sympy
#Instalar la librería NUMPY digitando en una consola de Windows: pip install numpy
#Instalar la librería IPYTHON digitando en consola de Windows: pip install ipython
#Instalar la librería CYTHON digitando en una consola de Windows: pip install cython
#Instalar la librería MATPLOTLIB y la funcionalidad para ejecutarse desde la
#consola de Windows digitando en ella: pip install matplotlib
#Con estas librerías instaladas se pueden importar correctamente los módulos
#necesarios

import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import trigsimp, sin, cos
#from matplotlib.pyplot import *





print("\n Por favor escribir la función de acuerdo a la sintaxis de la librería 'math' de Python \n")
strfuncion = input("Indicar la función que desea evaluar: \n")
strfuncionNewton = strfuncion.replace('math.', '')
strfuncionGraf = strfuncion.replace('math.','np.')


x = sp.Symbol('x')


job = input("Indicar si desea encontrar un mínimo o un máximo (min/max): \n")


print("\nParámetros del método de la sección dorada:")
xl = float(input("\t\tIndicar xl: " ))
xu = float(input("\t\tIndicar xu: " ))
precision = float(input("\t\tIndicar orden de magnitud de tolerancia (máximo igual a 10): "))


print("\nParámetros del método de la interpolación cuadrática:")
x0 = float(input("\t\tIndicar x0: " ))
x1 = float(input("\t\tIndicar x1: " ))
x2 = float(input("\t\tIndicar x2: " ))
preciss = int(input("\t\tIndicar cantidad de iteraciones: "))


print("\nParámetros del método de Newton:")
x0n = float(input("\t\tIndicar x0: " ))


def function(x_eval):
    x = x_eval
    fx = eval(strfuncion)
    return fx

if job == "min":
    minimo = True
    maximo = False
if job == "max":
    minimo = False
    maximo = True


################### CÓDIGO CORRESPONDIENTE AL MÉTODO DE LA SECCIÓN DORADA #############################


phi = (math.sqrt(5) - 1) / 2

def goldenRatio (x_l, x_u):

    x_uno = x_u - phi * (x_u - x_l)
    x_dos = x_l + phi * (x_u - x_l)

    fx_uno = function(x_uno)
    fx_dos = function(x_dos)

    return x_uno, x_dos, fx_uno, fx_dos

def tolerance(x_l, x_u):

    x_uno = x_u - phi * (x_u - x_l)
    x_dos = x_l + phi * (x_u - x_l)

    if abs(x_u - x_l) <  math.pow(10,-1) * precision * (abs(x_uno) + abs(x_dos)):
        return True
    else:
        return False

tolerancia = tolerance(xl, xu)
fxl = function(xl)
fxu = function(xu)
x1, x2, fx1, fx2 = goldenRatio(xl, xu)
#lista = ['{:.2f}'.format(x1), '{:.2f}'.format(x2), '{:.2f}'.format(fx1), '{:.2f}'.format(fx2)]


while tolerancia:
    if minimo:
        if fx1 > fx2:
            xl = x1
        if fx1 < fx2:
            xu = x2
        fxl = function(xl)
        fxu = function(xu)
        x1, x2, fx1, fx2 = goldenRatio(xl, xu)
        #lista = ['{:.2f}'.format(x1), '{:.2f}'.format(x2), '{:.2f}'.format(fx1), '{:.2f}'.format(fx2)]
        #print(lista)

    if maximo:
        if fx1 > fx2:
            xu = x2
        if fx1 < fx2:
            xl = x1
        fxl = function(xl)
        fxu = function(xu)
        x1, x2, fx1, fx2 = goldenRatio(xl, xu)
        #lista = ['{:.2f}'.format(x1), '{:.2f}'.format(x2), '{:.2f}'.format(fx1), '{:.2f}'.format(fx2)]
        #print(lista)

    tolerancia = tolerance(xl, xu)

print("\n\n#### Resultados correspondientes a la ejecución del método de la sección dorada ####")

if minimo:
    if fx1 > fx2:
        xfinal = x2
        print("Se ha estimado un mínimo alrededor de (" + str(xfinal) + ", " + str(fx2) + ")")
    if fx1 < fx2:
        xfinal = x1
        print("Se ha estimado un mínimo alrededor de (" + str(xfinal) + ", " + str(fx1) + ")")

if maximo:
    if fx1 > fx2:
        xfinal = x1
        print("Se ha estimado un máximo alrededor de (" + str(xfinal) + ", " + str(fx1) + ")")
    if fx1 < fx2:
        xfinal = x2
        print("Se ha estimado un máximo alrededor de (" + str(xfinal) + ", " + str(fx2) + ")")


################### FIN DEL CÓDIGO CORRESPONDIENTE AL MÉTODO DE LA SECCIÓN DORADA #############################


################### CÓDIGO CORRESPONDIENTE AL MÉTODO DE LA INTERPOLACIÓN CUADRÁTICA ###########################

def punto_x3(x0, x1, x2):
    fx0 = function(x0)
    fx1 = function(x1)
    fx2 = function(x2)

    termino1 = x1 ** 2 - x2 ** 2
    termino2 = x2 ** 2 - x0 ** 2
    termino3 = x0 ** 2 - x1 ** 2
    termino4 = x1 - x2
    termino5 = x2 - x0
    termino6 = x0 - x1

    x3 = (fx0 * termino1 + fx1 * termino2 + fx2 * termino3) / (2 * (fx0 * termino4 + fx1 * termino5 + fx2 * termino6))
    fx3 = function(x3)
    return x3, fx3, fx1

def tipo_extremo(x0, x1, x2):
    fx0 = function(x0)
    fx1 = function(x1)
    fx2 = function(x2)

    num1 = fx0 * (x2 - x1)
    num2 = fx1 * (x2 - x0)
    num3 = fx2 * (x1 - x0)

    num = num1 - num2 + num3

    den1 = x2 - x1
    den2 = x1 * x2 + x0 ** 2
    den3 = x0 * (x2 + x1)

    den = den1 * (den2 - den3)

    b = num / den

    if b > 0:
        tipo = "mínimo"
    elif b < 0:
        tipo = "máximo"
    return tipo


x3, fx3, fx1 = punto_x3(x0, x1, x2)

for iteracion in range(preciss):
    if fx3 > fx1:
        x0 = x1
        x1 = x3
        iteracion = iteracion + 1
        x3, fx3, fx1 = punto_x3(x0, x1, x2)
    if fx3 < fx1:
        x2 = x3
        iteracion = iteracion + 1
        x3, fx3, fx1 = punto_x3(x0, x1, x2)

#lista2 = ['{:.3f}'.format(x0), '{:.3f}'.format(x1), '{:.3f}'.format(x2)]

tipoextremo = tipo_extremo(x0, x1, x2)


print("\n\n#### Resultados correspondientes a la ejecución del método de la interpolación cuadrática ####")
print("Se ha estimado un " + tipoextremo + " alrededor de (" + str(x3) + ", " + str(fx3) + ")")


################### FIN DEL CÓDIGO CORRESPONDIENTE AL MÉTODO DE LA INTERPOLACIÓN CUADRÁTICA ###########################

##################################### CÓDIGO CORRESPONDIENTE AL MÉTODO DE NEWTON ######################################


def primeraderivada(x_eval):
    f_prima_x = sp.diff(strfuncionNewton)
    f_prima_x = f_prima_x.evalf(subs={x: x_eval})
    return f_prima_x

def segundaderivada(x_eval):
    f_prima_x = sp.diff(strfuncionNewton)
    f_segunda_x = sp.diff(f_prima_x)
    f_segunda_x = f_segunda_x.evalf(subs={x: x_eval})
    return f_segunda_x

def Newton(x_i):
    x_j = x_i - (primeraderivada(x_i) / segundaderivada(x_i))
    return x_j


f_prima_xi = primeraderivada(x0n)
f_segunda_xi = segundaderivada(x0n)
#error = 100 * abs(xcrit - x0n) / xcrit
xj = Newton(x0n)


while abs(primeraderivada(xj)) > math.pow(10,-15):
    xi = xj
    xj = Newton(xi)


print("\n\n#### Resultados correspondientes a la ejecución del método de Newton ####")
print("Se ha estimado un máximo alrededor de (" + str(xi) + ", " + str(function(xi)) + ")")

##################################### FIN DEL CÓDIGO CORRESPONDIENTE AL MÉTODO DE NEWTON ######################################
