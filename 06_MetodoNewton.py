#Instalar la librería tabulate usando pip install tabulate en una ventana del cmd de Windows

import math
from tabulate import tabulate

def funcion(x):
    fx = -0.3 * math.pow(x,4) + 1.2 * math.pow(x,3) - 1.8 * math.pow(x,2) + 4 * x
    return fx

def primeraderivada(x):
    f_prima_x = -1.2 * math.pow(x,3) + 3.6 * math.pow(x,2) - 3.6 * x + 4 #Derivada de la ecuación cuyo máximo desea conocerse
    #fx = 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4
    return f_prima_x

def segundaderivada(x):
    f_segunda_x = -3.6 * math.pow((x - 1),2)
    #dfx = 4 - 3.6 * x + 3.6 * x ** 2 - 1.2 * x ** 3
    return f_segunda_x

def Newton(x_i):
    x_j = x_i - primeraderivada(x_i) / segundaderivada(x_i)
    return x_j

tabla = []
encabezados = ['Iteración', 'xi', 'f(xi)', 'f´(xi)', 'f´´(xi)', 'Error (%)']

i = 1
xi = float(input("Indicar el valor de x inicial cercano a la raíz sospechada: "))
fxi = funcion(xi)
f_prima_xi = primeraderivada(xi)
f_segunda_xi = segundaderivada(xi)
xmax = 2.32635
error = 100 * abs(xmax - xi) / xmax
fila = [i, xi, fxi, f_prima_xi, f_segunda_xi, error]
tabla.append(fila)
xj = Newton(xi)
i = i + 1

while error > 1:
    xi = xj
    fxi = funcion(xi)
    f_prima_xi = primeraderivada(xi)
    f_segunda_xi = segundaderivada(xi)
    error = 100 * abs(xmax - xi) / xmax
    fila = [i, xi, fxi, f_prima_xi, f_segunda_xi, error]
    tabla.append(fila)
    xj = Newton(xi)
    i = i + 1

print("\n\n")
print(tabulate(tabla, headers = encabezados))
print("\n\nSe ha estimado una raíz alrededor de x = " + str(xi))
