def burbuja(lista):
    """
    Ordena una lista de elementos mediante el algoritmo de burbuja.

    La burbuja es un algoritmo de ordenamiento que funciona de la siguiente
    manera:

    - Primero, se toma el primer elemento de la lista como pivote.
    - Luego, se busca el elemento mas pequeño al lado del pivote y se
    intercambia con el pivote.
    - Despues, se sigue buscando el elemento mas pequeño en el resto de la
    lista y se intercambia con el elemento que esta al lado del pivote.
    - Asi sucesivamente, se sigue hasta que la lista esta ordenada.

    :param lista: La lista que se va a ordenar
    :return: La lista ordenada
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                apoyo = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = apoyo
    return lista            
    
numeros = [51,42,74,1,10]
burbuja(numeros)

print(numeros)