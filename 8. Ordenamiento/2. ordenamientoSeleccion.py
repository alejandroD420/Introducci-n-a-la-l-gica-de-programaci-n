def selection_sort(lista):
    """
    Ordena una lista de elementos mediante el algoritmo de selecci n.

    La seleccion es un algoritmo de ordenamiento que funciona de la siguiente
    manera:

    - Primero, se busca el elemento minimo en la lista.
    - Luego, se intercambia con el primer elemento de la lista.
    - Despues, se busca el elemento minimo en el resto de la lista y se
    intercambia con el segundo elemento de la lista.
    - Asi sucesivamente, se sigue hasta que la lista esta ordenada.

    :param lista: La lista que se va a ordenar
    :return: La lista ordenada
    """
    tamanna = len(lista)
    for i in range(tamanna):
        min_idx = i
        for j in range(i+1,tamanna):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i] , lista[min_idx] = lista[min_idx], lista[i]
    return lista



numeros = [51,42,74,1,10]
print(selection_sort(numeros))