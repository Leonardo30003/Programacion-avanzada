"""Escribir una función que calcule el área de un círculo y otra que calcule el volumen 
de un cilindro usando la primera función."""


def areaCirculo(radius):
    pi = 3.1415
    return pi*radius**2


def volmenCilindro(radius, high):
    return areaCirculo(radius)*high
print(volmenCilindro(3, 5))
