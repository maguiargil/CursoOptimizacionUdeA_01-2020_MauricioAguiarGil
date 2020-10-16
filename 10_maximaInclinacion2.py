import sympy as sp
import numpy as np

from sympy import *
from sympy.solvers import solve

n = int(input("Indicar la cantidad de iteraciones deseadas: "))
x0 = float(input("Indicar el valor inicial de búsqueda para x0: "))
y0 = float(input("Indicar el valor inicial de búsqueda para y0: "))

print("\nPor favor escribir la función de acuerdo a la sintaxis de la librería 'sympy' de Python \n")
funcion = input("Indicar la función que desea evaluar: \n")


x, y, h = sp.symbols('x y h')


def function(x_eval, y_eval):
    x = x_eval
    y = y_eval
    fx = eval(funcion)
    return fx

def primeraderivada(f, x_0, y_0):
    fx = diff(f, x)
    fy = diff(f, y)
    fx_eval = fx.subs(x,x_0).subs(y,y_0)
    fy_eval = fy.subs(x,x_0).subs(y,y_0)
    return fx_eval, fy_eval

def transformacion(x_cero, y_cero, fxeval, fyeval):
    x_nuevo = x_cero + fxeval * h
    y_nuevo = y_cero + fyeval * h
    return x_nuevo, y_nuevo

def maximaInclinacion(f_transformada, x_0, y_0):
    gprima = diff(f_transformada, h)

    h_optimo_finiteSet = N(sp.solveset(gprima, h, domain = S.Reals), 20)

    h_optimo = list(h_optimo_finiteSet)

    fxeval, fyeval = primeraderivada(funcion, x_0, y_0)
    x0 = x_0 + fxeval * h_optimo[0]
    y0 = y_0 + fyeval * h_optimo[0]
    return x0, y0

def segundaderivada(x_eval, y_eval):
    f_prima_x = sp.diff(strfuncionMaxInclin)
    f_segunda_x = sp.diff(f_prima_x)
    f_segunda_x = f_segunda_x.evalf(subs={x: x_eval})
    return f_segunda_x

for i in range(n):
    fx1, fy1 = primeraderivada(funcion, x0, y0)
    x1, y1 = transformacion(x0, y0, fx1, fy1)
    g = function(x1, y1)
    x0, y0 = maximaInclinacion(g, x0, y0)

z = function(x0, y0)
print("\nSe ha estimado un punto crítico en (x , y , z) = (" + str(x0) + ", " + str(y0) + ", " + str(z) + ")")
