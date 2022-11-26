"""Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas."""

contrasenia = "criaturitasdelseñor"
contraseniaUsuario = input("Introduce la contraseña: ")
if contrasenia == contraseniaUsuario.lower():
    print("La contaseña es la correcta")
else:
    print("Estas equivocado loquito")