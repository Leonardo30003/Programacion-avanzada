"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años 
que ha cumplido (desde 1 hasta su edad)."""
edad = int(input("Ingrese su edad:"))
edadInicio = 1
while edadInicio <= edad:
    print("Usted cumplio",edadInicio)
    edadInicio = edadInicio+1
