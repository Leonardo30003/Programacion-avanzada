"""
Pedir una nota al usuario
Si la nota es menor a 10 y mayor o igual a 9, imprimir Exelente.
si la nota es menor a 9 y mayor o igual a 8, imprimir Muy bueno
si la nota es menor a 8 y mayor o igual a 7, imprimir bueno,
si la nota es menor a 7m imprimir reprobado
"""
nota= int(input("ingrese su nota: "))
def CalcularNota(notas):
    global nota

if nota>=9 and nota <= 10:
    print(f"{nota:} Exelente")
elif nota>=8 and nota<9:
    print(f"{nota:} Muy Bueno")
elif nota>=7 and nota<8:
    print(f"{nota:} Bueno")
elif nota<7:
    print(f"{nota:} Reprobado")
else:
    print("Calificacion desconocida")

