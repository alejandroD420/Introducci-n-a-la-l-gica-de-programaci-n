'''
Hacer un programa donde se ingrese un numero, verificar si el numero es pa o impar.
'''

a = float(input("Ingresar un numero"))

if a % 2 == 0:
    print(f"{a} es par")
elif a % 3 ==0:
    print(f"{a} es impar")
else:
    print(f"{a} es uno")