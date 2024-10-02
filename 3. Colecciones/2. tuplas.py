'''
Tuplas

Es una coleccion ordenada inmutable (No modificable)

Caracteristicas:

1. Son ordenadas
2. No son mutables
3. Pueden contener datos duplicados
4. Los elementos pueden ser diferentes tipos de datos
'''

# Definicion de una tupla
mi_tupla = (10, 20, 30, 40, "Hola")

# Acceder a un elemento concreto de la tupla
print(mi_tupla[3]) # Salida 40

# Modificar elemento de una lista
mi_tupla[3] = "adios" # Salida [10, 20, 30, "adios", "Hola"]

# Agregar elemento a la lista
#mi_tupla.append(50) # Esto genera un error: TypeError

# Eliminar elemento de una lista
#mi_tupla.remove(10) # Esto genera un error: TypeError

# Obtener longitud de una tupla
print(len(mi_tupla))

'''
Operadores

$ len(): Devuelve el tamaño de la lista
'''


