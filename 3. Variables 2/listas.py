''' Listas
Una lista  es una coleccion ordenada mutable (Se puede modificar) y 
pueden almacenar elementos de cualquier tipo.

Caracteristicas:

1. Son ordenadas
2. Son mutables
3. Pueden contener datos duplicados
4. Los elementos pueden ser diferentes tipos de datos
'''

# Definicion de una lista
mi_lista = [10, 20, 30, 40, "Hola"]

# Imprimir una lista
print(mi_lista) 

# Acceder a un elemento concreto de la lista
print(mi_lista[3]) # Salida 40

# Modificar elemento de una lista
mi_lista[3] = "adios" # Salida [10, 20, 30, "adios", "Hola"]

# Agregar elemento a la lista
mi_lista.append(50) # Salida [10, 20, 30, "adios", "Hola", 50]

# Eliminar elemento de una lista
mi_lista.remove(10) # Salida [20, 30, "adios", "Hola", 50]


# Obtener longitud de una lista
print(len(mi_lista))

'''
Operadores

$ append(): Agregar un elemento al final de la lista
$ remove(): Elimina el primer elemento que coincida de la lista
$ len(): Devuelve el tamaño de la lista
'''