#Sin parametros

def decir_hola():
    return "Hola!"

print(decir_hola())

#Con parametro

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado


def multiplicacion(a, b):
    resultado = a * b
    return resultado


def division(a, b):
    resultado = a / b
    return resultado


def potenciacion(a, b):
    resultado = a ** b
    return resultado

def raiz(a, b):
    resultado = a ** (1/b)
    return resultado




print(suma(25, 35))
print(resta(45, 35))
print(multiplicacion(5, 12))
print(division(45, 9))
print(potenciacion(2, 5))
print(raiz(49, 2))


#Funcion que no devulve valores
def imprimir_suma(a,b):
    print (a + b)

imprimir_suma(5,6)