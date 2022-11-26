"""Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones 
correspondientes a las notas."""


def grade(valor0a10):

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


def aplicarGrado(valor0a10):

    return {subject.upper(): grade(score) for subject, score in valor0a10.items()}


print(aplicarGrado({'Matemáticas': 6.5, 'Física': 5, 'Química': 3.4,
      'Economía': 8.2, 'Historia': 9.7, 'Programación': 10}))
