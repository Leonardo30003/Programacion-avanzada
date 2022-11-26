"""Escribir un programa que lea la puntuación e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario."""

bonificacion = 2400
inaceptable = 0
aceptable = 0.4
meritorio = 0.6
puntuacion = float(input("Introduce tu puntuación: "))
# Clasifiación por niveles de rendimiento
if puntuacion == inaceptable:
    nivel = "Inaceptable"
elif puntuacion == aceptable:
    nivel = "Aceptable"
elif puntuacion >= 0.6:
    nivel = "Meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobrar %.2f$" % (puntuacion * bonificacion))
