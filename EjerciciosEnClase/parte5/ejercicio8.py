"""Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario 
con su media, varianza y desviación típica."""


def square(listaNumeros):

    list = []
    for i in listaNumeros:
        list.append(i**2)
    return list


def statistics(listaNumeros2):

    stat = {}
    stat['media'] = sum(listaNumeros2)/len(listaNumeros2)
    stat['varianza'] = sum(square(listaNumeros2)) / \
        len(listaNumeros2)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat


print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
