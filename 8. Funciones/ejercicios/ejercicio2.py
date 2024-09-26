'''
Sistema de gestion  de estudiantes

Crea un sistema  que permita agregar, ver y eliminar de una lista. Usa
funciones para las operaciones de agregar, mostrar y borrar  estudiantes
'''

def agregar_estudiante():
    print("----------------Agregar Estudiantes-------------")
    identificacion = input("Ingrese numero de documento del estudiante: ")
    tipo_id = input("Ingrese tipo de documento del estudiante (cc/ti): ").lower()
    nombre = input("Ingrese nombre del estudiante: ").capitalize()
    apellido = input("Ingrese apellido del estudiante: ").capitalize()
    
    if tipo_id == 'cc' or tipo_id == 'ti':
        estudiantes.append({"identificacion": identificacion, "tipo_id": tipo_id, "nombre": nombre, "apellido": apellido})
        
        print("Estudiante agregado con exito")
    else:
        print("Error: Tipo de documento no valido")
    pass

def mostrar_estudiante():
    
    for i in estudiantes:
        
        print("----------------Mostrar Estudiantes-------------")
        
        print(f"ESTUDIANTE NUMERO {i+1}")
        
        if not estudiantes:
            print("No hay estudiantes")
            
        else:        
            print(f"Tipo de ocumento: {estudiantes["tipo_id"]} \n Documento: {estudiantes["identificacion"]} \n Nombre: {estudiantes["nombre"]} \n Apellido: {estudiantes["apellido"]}")
    pass

def eliminar_estudiante():
    print("----------------Eliminar Estudiantes-------------")
    
    
    estudiantes.clear()
    print("Estudiante eliminado exitosamente")
    pass

def menu():
    print("1. Agregar estudiante")
    print("2. Mostrar estudiante")
    print("3. Eliminar estudiante")
    print("4. Salir")
    
    

def buscar_estudiante(estudiantes, identificacion_estudiante_buscar):
    for estudiante in estudiantes:
        pass
    pass

estudiantes = []

while True:
    menu()
    opcion = int(input("Elige una opcion"))
    
    if opcion == 1:
        agregar_estudiante(estudiantes)
        pass
    elif opcion == 2:
        mostrar_estudiante(estudiantes)
    elif opcion == 3:
        eliminar_estudiante(estudiantes)
    elif opcion == 4:
        break
    else:
        print("Error: Opcion no valida")
    