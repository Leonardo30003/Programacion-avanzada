# crear una funcion que permita conocer el rango de edad de una persona
nombre = input("Ingrese su nombre: ")
print(type(nombre))
edad = int(input("Ingrese su edad: "))
print(type(edad))


def edadCalcular(int: edad):

    if edad >= 18 and edad <= 65:
        print(nombre, "es mayor de edad ")
    elif edad >= 65:
        print(nombre, "es tercera edad")
    else:
        print("es menor de edad")


edadCalcular(edad)
