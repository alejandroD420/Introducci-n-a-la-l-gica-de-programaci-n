while True:
    try:
        numero = input("Ingrese su nombre: ")
        telefono = int(input("Ingrese su telefono: "))
        print("Usuario registrado")
        break

    except:
        print("Dato no valido")
        print("Intenta de nuevo")   