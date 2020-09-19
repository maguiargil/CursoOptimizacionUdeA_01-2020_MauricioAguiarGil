import math

def funcion(x):
    fx = -9 * math.pow(x,5) -8 * math.pow(x,4) + 12 #Ecuación cuya raíz desea conocerse
    #fx = 3*math.pow(x,2) - 120 * x + 100
    return fx


xl = float(input("Indicar xl: "))
xu = float(input("Indicar xu: "))


while funcion(xl) * funcion(xu) > 0:
    xl = float(input("Indicar algún otro xl: "))
    xu = float(input("Indicar algún otro xu: "))

print("Los valores xl y xu satisfacen la condición inicial de que en ellos cambia signo\n")

xr = (xl + xu) / 2

probe = funcion(xl) * funcion(xr)
#  error_estimacion = abs(funcion(xl) - funcion(xr))

while probe != 0:

    if probe < 0:
        xu = xr
        xr = (xl + xu) / 2
        #print("Raíz en el subintervalo izquierdo\n")
        probe = funcion(xl) * funcion(xr)

    if probe > 0:
        xl = xr
        xr = (xl + xu) / 2
        #print("Raíz en el subintervalo derecho\n")
        probe = funcion(xl) * funcion(xr)

print("Se ha encontrado una raíz entre x = " + str(xl) + " y x = " + str(xu) + " ubicada en x = " + str(xr))
