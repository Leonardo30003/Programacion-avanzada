"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n>
 entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos 
 por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente."""
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese otro numero: "))
cociente=numero1%numero2
resta=numero1//numero2
print("El cociente es ",cociente)
print("La resta es ",resta)