"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""
inversion = float(input("Ingrese cantidad a invertir:"))
interes = float(input("Ingrese el interés porcentual anual:"))
anios = int(input("Cuantos años desea invertir:"))
for i in range(anios):
    inversion *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(inversion, 2)))