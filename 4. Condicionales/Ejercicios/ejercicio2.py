'''
Hacer un programa donde se ingrese un numero, verificar sin el numero es positivo, negativo o cero.
'''

a = float(input("Ingresar un numero"))

if a > 0:
    print("El numero es positivo")
elif a < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")