"""Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes 
a las notas aprobadas."""
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

def aplicarNota(valor0a10):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    sujetos = map(str.upper, valor0a10.keys())
    notas = map(grade, valor0a10.values())
    return dict(zip(sujetos, notas))

print(aplicarNota({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))
