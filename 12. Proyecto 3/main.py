usuarios = {
    "usuario1" : {"contrasenia": "123", "saldo": 1000},
    "usuario2" : {"contrasenia": "456", "saldo": 2000},
    "usuario3" : {"contrasenia": "789", "saldo": 3000},
    "usuario4" : {"contrasenia": "321", "saldo": 4000},
    "usuario5" : {"contrasenia": "654", "saldo": 5000}
}

'''
Funcion para autenticar si el susuario tiene asociada la misma contraseña
'''
def autenticarUsuario(nombre, contrasenia):
    """Determina si el usuario tiene la contrasenia asociada
    
    Parameters:
    nombre (str): El nombre del usuario
    contrasenia (str): La contrasenia del usuario
    
    Returns:
    bool: True si el usuario se autentica, False en caso contrario
    """
    usuario = usuarios.get(nombre)
    if usuario and usuario.get("contrasenia") == contrasenia:
        return True
    return False

'''
Funcion para consultar el saldo de un usuario
'''
def consultarSaldo(usuario):
    """Devuelve el saldo actual de un usuario
    
    Parameters:
    usuario (dict): El usuario que se va a consultar
    
    Returns:
    int: El saldo actual del usuario
    """
    return usuario.get("saldo")

'''
Funcion para extraer dinero de la cuenta de un usuario
'''
def extraerDinero(usuario, cantidad):
    """Extrae dinero de la cuenta de un usuario
    
    Parameters:
    usuario (dict): El usuario al que se le va a extraer el dinero
    cantidad (int): La cantidad de dinero a extraer
    
    Returns:
    str: El mensaje de resultado de la extraccion
    """
    if cantidad <= 0:
        if cantidad <= usuario.get("saldo"):
            usuario["saldo"] -= cantidad
            return f"Dinero extraido: {cantidad} de tu cuenta"
        return "No hay saldo suficiente"
    return "La cantidad a extraer no existe"

'''
Funcion para depositar dinero en la cuenta de un usuario
'''
def depositarDinero(usuario, cantidad):
    """Deposita dinero en la cuenta de un usuario
    
    Parameters:
    usuario (dict): El usuario al que se le va a depositar el dinero
    cantidad (int): La cantidad de dinero a depositar
    
    Returns:
    str: El mensaje de resultado del deposito
    """
    if cantidad > 0:
        usuario["saldo"] += cantidad
        return f"Dinero depositado: {cantidad} en tu cuenta"
    return "La cantidad a depositar no existe"

'''
Funcion para cambiar la contrasenia de un usuario
'''
def cambiarContrasenia(usuario, contrasenia):
    """Cambia la contrasenia de un usuario si la contrasenia digitada coincide con la que esta en el registro
    
    Parameters:
    usuario (dict): El usuario al que se le va a cambiar la contrasenia
    contrasenia (str): La contrasenia actual del usuario
    
    Returns:
    str: El resultado de la operacion, indica si se ha cambiado con exito o no
    """
    if usuario.get("contrasenia") == contrasenia:
        nuevaContrasenia = input("Introduce la nueva contrasenia: ")
        usuario["contrasenia"] = nuevaContrasenia
        return "La contarseña se ha cambiado con exito"
    return "La contrasenia digitada es incorrecta"

''' Creacion de menu en bucle while true, y uso de funciones creadas
Creacion de menu que permita autenticar si el usuario esta creado y luego de autenticarlo me va a permitir continuar o no
'''

def menu():
    """
    Menu principal de la aplicacion, permite autenticar y una vez autenticado
    permite realizar operaciones de consultar saldo, retirar dinero, depositar dinero
    y salir
    """
    while True:
        nombre = input("Introduce su nombre o (salir) para finalizar: ")
        if nombre.lower() == "salir":
            break
        contrasenia = input("Introduce su contrasenia: ")
        autenticado = autenticarUsuario(nombre, contrasenia)
        if not autenticado:
            print("Usuario o contrasenia incorrectos")
            continue
        print("Bienvenido", nombre)
        while True:
            print("----------- MENÚ -----------")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Depositar dinero")
            print("4. Salir")
            print("-----------------------------")
            try:
                opcion = int(input("Introduce una opcion: "))
                if opcion == 1:
                    print("Su saldo es:", consultarSaldo(usuarios[nombre]))
                elif opcion == 2:
                    cantidad = int(input("Introduce la cantidad a retirar: "))
                    print(extraerDinero(usuarios[nombre], cantidad))
                elif opcion == 3:
                    cantidad = int(input("Introduce la cantidad a depositar: "))
                    print(depositarDinero(usuarios[nombre], cantidad))
                elif opcion == 4:
                    print("Hasta pronto")
                    break
            except Exception as e:
                print("Opcion invalida")
                print(e)
                