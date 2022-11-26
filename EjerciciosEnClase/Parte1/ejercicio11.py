"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento 
del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del 
día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que 
se le hace por no ser fresca y el coste final total."""

PanVendido = float(input("Cuantos panes desea comprar: "))
pan = 3.49
panNoDia = 60/100
panConDescuento = (PanVendido*pan)*(1-panNoDia)
print("Precio unidad de pan:", pan,"$", '\n' "Descuento por unidad de pan", panNoDia*100,"%",
      '\n' "Precio final", panConDescuento,"$")
