def calcula_factorial(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado

print(calcula_factorial(5))

def calcula_factorial2(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(calcula_factorial2(5))


