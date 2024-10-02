# Calcular cual numero es mayor

a = float(input("Ingrese el primer numero"))
b = float(input("Ingrese el segundo numero"))

if a == b:
    print(f"{a} es igual {b}")
elif a > b:
    print(f"{a} es mayor que {b}")
else:
    print("Los numeros son iguales")