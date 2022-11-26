"""Escribir una función que reciba una frase y devuelva un
diccionario con las palabras que contiene y su longitud."""

def longitudPalabras(sentencia):

    return {palabra:len(palabra) for palabra in sentencia.split()}

print(longitudPalabras('Welcome to Python'))
