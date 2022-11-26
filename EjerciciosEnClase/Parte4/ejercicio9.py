#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
numero = int(input("Introduce un número entero positivo: "))
i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print(str(numero) + " es primo")
else:
    print(str(numero) + " no es primo")