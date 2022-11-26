"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos
 iguales o superiores a $1000 mensuales. Escribir un programa que pregunte al usuario su edad
  y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no."""

nombre=input("Ingrese su nombre:")
edad=int(input("Ingrese su edad:"))
ingresos=float(input("Ingrese su sueldo mensual:"))
if edad>=16 and ingresos>=1000:
    print(nombre,"tiene que tributar")
else:
    print(nombre,"no tiene que tributar")