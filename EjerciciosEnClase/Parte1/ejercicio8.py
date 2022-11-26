"""Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
el número de años, y muestre por pantalla el capital obtenido en la inversión."""

invercion = float(input("cuanto desea invertir"))
interesAnual = 12
numeroAñosInvercion = int(input("cuantos años desea invertir ?"))

capital = (invercion*12/100*numeroAñosInvercion)
print(capital)
