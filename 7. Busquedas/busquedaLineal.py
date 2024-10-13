def busqueda_lineal(objeto,lista):
    """
    Realiza una busqueda lineal en una lista y devuelve el indice
    del elemento si se encuentra, si no devuelve None.

    :param objeto: El elemento a buscar
    :param lista: La lista en la que buscar
    :return: El indice del elemento si se encuentra, None en caso contrario
    """
    for i in range(len(lista)):
        if lista[i] == objeto:
            return i #Devuelve el indice del elemento

#Ejemplo de uso
numeros = [10, 20 ,30,45,90,11,22]

resultado = busqueda_lineal(45,numeros)

if resultado:
    print("Elemento encontrado")
    
else:
    print("Elemento no encontrado")