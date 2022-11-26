"""Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
 Si el divisor es cero el programa debe mostrar un error."""

Dividendo = float(input("Introduce el dividendo: "))
Divisor = float(input("Introduce el divisior: "))
division=int(Dividendo/Divisor)
if division == 0:
    print("Syntaxis Error")
else:
    print(Dividendo/Divisor)