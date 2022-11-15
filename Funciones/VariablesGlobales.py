salario = int(input("Por favor ingrese su salario: "))


def calcularSalario(int:salario):
    global salario
    #salario = 300
    seguro = 50
    salarioTotal = salario-seguro
    return salarioTotal
print(calcularSalario(salario))