def operaciones(a, b):
    
    numero1 = a
    numero2 = b
    
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b


    def multiplicacion(a, b):
        return a * b


    def division(a, b):
        return a / b

    def potenciacion(a, b):
        return a ** b

    def raiz(a, b):
        return a ** (1/b)
    
    resultado_suma = suma(numero1, numero2)
    resultado_resta = resta(numero1, numero2)
    resultado_multiplicacion = multiplicacion(numero1, numero2)
    resultado_division = division(numero1, numero2)
    resultado_potenciacion = potenciacion(numero1, numero2)
    resultado_raiz = raiz(numero1, numero2)
    
    return (f"El resultado de la suma es {resultado_suma}, 
\n El resultado de la resta es {resultado_resta}, El resultado de la multiplicacion es {resultado_multiplicacion}, El resultado de la division es {resultado_division}, El resultado de la potenciacion es {resultado_potenciacion}, El resultado de la raiz es {resultado_raiz}")
print(operaciones(2, 3))

