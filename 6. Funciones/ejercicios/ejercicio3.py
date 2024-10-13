def validarNumero(numero):
    """
    Verifica si un numero es par o impar, si es par
    devuelve un string con el numero y el mensaje "es par" y
    un mensaje de despedida, si es impar devuelve un string con
    el numero y el mensaje "es impar" y un mensaje de despedida,
    si no cumple con ninguna de las condiciones devuelve False
    """
    numero = int(numero)
    if numero % 2 == 0 and numero != 0:
        return f"{numero} es par \n----------------------ADIOS--------------------- \n"   
    elif numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        return f"{numero} es impar \n----------------------ADIOS--------------------- \n"
    else:
        return False
    
def main():
    """
    Muestra un mensaje de bienvenida, solicita un numero al usuario,
    si el numero es 0 sale del bucle, si es un numero par, impar o
    multiplo de 3,5 o 7 imprime un mensaje con el numero y su
    condicion correspondiente y un mensaje de despedida, si no cumple
    con las condiciones anteriores imprime un mensaje de error
    """
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