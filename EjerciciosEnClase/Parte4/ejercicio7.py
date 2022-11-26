"""Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo."""
alturaTriangulo = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(alturaTriangulo):
    for j in range(i+1):
        print(alturaTriangulo, end="")
    print("")
