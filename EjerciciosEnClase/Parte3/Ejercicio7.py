"""Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el 
tipo impositivo que le corresponde."""

nombre=input("Ingrese su nombre:")
renta=float(input("Ingrese su renta anual"))
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
print(nombre,"Tienes que pagar ", renta * tipo / 100)