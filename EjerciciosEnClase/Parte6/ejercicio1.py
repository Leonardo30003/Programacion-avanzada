"""Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta
de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos 
o el IVA a los productos de la cesta y devolver el precio final de la cesta."""


def aplicarDescuento(precio, descuento):

    return precio - precio * descuento / 100


def aplicarIva(precio, porcentaje):

    return precio + precio * porcentaje / 100


def precioBasquet(basket, funcion):

    total = 0
    for precio, descuento in basket.items():
        total += funcion(precio, descuento)
    return total


print('El precio de la compra tras aplicar los descuentos es: ',
      precioBasquet({1000: 20, 500: 10, 100: 1}, aplicarDescuento))
print('El precio de la compra tras aplicar el IVA es: ',
      precioBasquet({1000: 20, 500: 10, 100: 1}, aplicarIva))
