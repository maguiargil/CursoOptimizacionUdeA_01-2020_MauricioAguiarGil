from random import seed
from random import random
import math
import sympy

seed(1)

n = int(input("Indicar la cantidad de iteraciones deseada: "))
xl = float(input("Indicar el límite inferior en x = xl: "))
xu = float(input("Indicar el límite superior en x = xu: "))
yl = float(input("Indicar el límite inferior en y = yl: "))
yu = float(input("Indicar el límite superior en y = yu: "))

print("\n Por favor escribir la función de acuerdo a la sintaxis de la librería 'math' de Python \n")
strfuncion = input("Indicar la función que desea evaluar: \n")
strfuncionRandom = strfuncion.replace('math.', '')

x = sympy.Symbol('x')
y = sympy.Symbol('y')

job = input("Indicar si desea encontrar un mínimo o un máximo (min/max): \n")

def function(x_eval, y_eval):
	x = x_eval
	y = y_eval
	fx = eval(strfuncion)
	return fx

if job == "min":
	minimo = True
	maximo = False
	minf = math.pow(10,9)
	strjob = "Mínimo "
if job == "max":
	minimo = False
	maximo = True
	maxf = math.pow(-10,9)
	strjob = "Máximo "

for j in range(n):
	x = xl + (xu - xl) * random()
	y = yl + (yu - yl) * random()
	fn = function(x,y)
	if maximo:
		if fn > maxf:
			maxf = fn
			maxx = x
			maxy = y
	if minimo:
		if fn < minf:
			minf = fn
			minx = x
			miny = y

if maximo:
	print(strjob + "en (x , y , z) = (" + str(maxx) + ", " + str(maxy) + ", " + str(maxf) + ")")
else:
	print(strjob + "en (x , y , z) = (" + str(minx) + ", " + str(miny) + ", " + str(minf) + ")")
