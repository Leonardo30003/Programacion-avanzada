"""Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y 
devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje 
de IVA, deberá aplicar un 21%."""


def iva(cantidad, porcentajeIva=21):

    return cantidad + cantidad*porcentajeIva/100

print(iva(100, 12))
print(iva(1000))
