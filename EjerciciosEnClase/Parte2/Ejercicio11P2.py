"""Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades 
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 
6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 
dígitos enteros y 2 decimales."""

producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario 6 digitos y dos decimales: '))
unidades = int(input('Introduce el número de unidades con 3 digitos : '))
print("El nombre del producto es:",producto,"\n"
"El precio unitrio del producto es:",precio,"\n"
"El numero de unidades es:",unidades,"\n"
"El coste total es:",float(unidades*precio))