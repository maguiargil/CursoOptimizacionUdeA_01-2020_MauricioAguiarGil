#Instalar la librería tabulate usando pip install tabulate en una ventana del cmd de Windows

import math
from tabulate import tabulate

def funcion(x):
    fx = -9 * math.pow(x,5) -8 * math.pow(x,4) + 12 #Ecuación cuya raíz desea conocerse
    #fx = 4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4
    return fx

def derivada(x):
    dfx = -1 * math.pow(x,3) * (45 * x + 32)
    #dfx = 4 - 3.6 * x + 3.6 * x ** 2 - 1.2 * x ** 3
    return dfx

def newtonRaphson(x_i):
    x_j = x_i - funcion(x_i) / derivada(x_i)
    return x_j

tabla = []
encabezados = ['Iteracion', 'xi', 'Error (%)']

i = 1
xi = float(input("Indicar el valor de x inicial cercano a la raíz sospechada: "))
zero = 0.926
error = 100 * abs(zero - xi) / zero
fila = [i, xi, error]
tabla.append(fila)
xj = newtonRaphson(xi)
i = i + 1

while error > 1:
    xi = xj
    error = 100 * abs(zero - xi) / zero
    fila = [i, xi, error]
    tabla.append(fila)
    xj = newtonRaphson(xi)
    i = i + 1

print("\n\n")
print(tabulate(tabla, headers = encabezados))
print("\n\nSe ha estimado una raíz alrededor de x = " + str(xi))
