def validarNumero(numero):
    numero = int(numero)
    if numero % 2 == 0 and numero != 0:
        return f"{numero} es par"    
    elif numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        return f"{numero} es impar"
    else:
        return False
    
def main():
    while True:
        try:
            print("-------------------BIENVENIDO-------------------")
            numero = int(input("Ingresar un numero O (0) para salir: "))
            if numero == 0:
                break
            print(validarNumero(numero))
        except ValueError:
            print("El valor no es un numero")
            
main()