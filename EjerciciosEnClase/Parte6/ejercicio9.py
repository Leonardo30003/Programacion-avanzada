# Escribir una función que calcule el módulo de un vector.
def suma(x, y):

    return x + y ** 2


def modulo(v):

    from functools import reduce
    return reduce(suma, v, 0) ** 0.5


print(modulo((3, 4)))
print(modulo((1, 2, 3)))
