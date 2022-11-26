"""Escribir una función que calcule el máximo común divisor de dos números y otra que
 calcule el mínimo común múltiplo."""

def maximoComunDivisor(n, m):

    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def minimoComunMultiplo(n, m):

    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(maximoComunDivisor(24,36))
print(minimoComunMultiplo(24,36))