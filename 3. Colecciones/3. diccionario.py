'''
Diccionarios

Es una coleccion desordenada de pares Clave-valor, donde cada Clave debe ser unica y
estar asociada a un valor, se utiliza para representar relaciones de datos, como una tabla.  

Caracteristicas:

1. Los elementos de almacenan como pares Clave-Valor
2. Las claves son inmutables
3. Las claves deben ser unicas, pero los valores pueden repetirse
4. Los elementos pueden ser diferentes tipos de datos
'''
# Definicion de diccionarios
mi_diccionario = {
    "nombre": "Ruben Alejandro",
    "edad": 22,
    "ciudad": "Caracas",
    "idiomas": ["Ingles", "Frances", "Español"],
    "grupoSanguineo": None
}

# Imprimir un diccionario
print(mi_diccionario) # Salida {'nombre': 'Ruben Alejandro', 'edad': 22, 'ciudad': 'Caracas', 'idiomas': ['Ingles, Frances, Español'], 'grupoSanguineo': None}

# Acceder a un elemento concreto del diccionario mediante su clave
print(mi_diccionario["nombre"]) # Salida "Ruben Alejandro"

# Modificar elemento de un diccionario
mi_diccionario["edad"] = 27 # Salida {'nombre': 'Ruben Alejandro', 'edad': 27, 'ciudad': 'Caracas', 'idiomas': ['Ingles, Frances, Español'], 'grupoSanguineo': None}

# Agregar un nuevo par clave-valor al diccionario
mi_diccionario["profesion"] = "Estudiante" # Salida {'nombre': 'Ruben Alejandro', 'edad': 27, 'ciudad': 'Caracas', 'profesion': 'Estudiante', 'idiomas': ['Ingles, Frances, Español'], 'grupoSanguineo': None}

# Eliminar un par clave-valor al diccionario
del mi_diccionario["ciudad"] # Salida {'nombre': 'Ruben Alejandro', 'edad': 22, 'idiomas': ['Ingles, Frances, Español'], 'grupoSanguineo': None}

# Imprimir un elemento de una lista en un diccionario
print(mi_diccionario["idiomas"][2])

'''
Operadores

$ del(): Elimina un par Clave-Valor
'''


