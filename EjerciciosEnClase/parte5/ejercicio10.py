"""Escribir una función que convierta un número decimal en binario y otra que 
convierta un número binario en decimal."""


def cambiarADecimal(n):

    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal


def CambiarABinario(n):

    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)


print(cambiarADecimal('10110'))
print(CambiarABinario(22))
print(cambiarADecimal(CambiarABinario(22)))
print(CambiarABinario(cambiarADecimal('10110')))
