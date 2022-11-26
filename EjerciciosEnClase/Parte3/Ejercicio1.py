"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""

edad=int(input("Ingrese su edad: "))
mayorEdad=18
if edad>=mayorEdad:
    print("Es mayor de edad")
else:
    print("Es menor de edad")