"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
 calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa
  debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente 
  es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor 
  de 18 años, $10."""

cliente=int(input("Ingrese su edad:"))
if cliente<4:
    print("Puede entrar gratis")
elif cliente==4 or cliente<18:
    print("Precio a pagar son 5 dolares")
elif cliente>18:
    print("Debe pagar 10 dolares")