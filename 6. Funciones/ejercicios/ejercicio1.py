'1. Calculadora con un diccionario'

def suma(x, b):
    return x + b

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(a, b):
    if y != 0:
        return x * y
    else:
        return "Error: division por cero"

def potenciacion(a, b):
    return a ** b

def raiz(a, b):
    return a ** (1/b)

def menu():
    print("Seleccionar una operacion: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potenciacion")
    print("6. Raiz")
    print("7. Salir")

operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: potenciacion,
    6: raiz
}
while True:
    menu()
    opcion = int(input("Selecciona una operacion: "))
    
    if opcion in operaciones:
        
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el segundo numero: "))

        resultado = operaciones[opcion](numero1, numero2)
        
        print(f"El resultado es: {resultado}")

    elif opcion == 6:
        break
    else:
        print("Eror: Opcion no valida...")



