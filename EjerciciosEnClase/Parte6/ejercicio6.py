"""Escribir una función reciba una lista de notas y devuelva la lista de 
calificaciones correspondientes a esas notas."""


def grado(valor0a10):

    if valor0a10 < 5:
        return 'SS'
    elif valor0a10 < 7:
        return 'AP'
    elif valor0a10 < 9:
        return 'NT'
    elif valor0a10 < 10:
        return 'SB'
    else:
        return 'MH'


def aplicarNota(listaDe0a10):

    return list(map(grado, listaDe0a10))


print(aplicarNota([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))
