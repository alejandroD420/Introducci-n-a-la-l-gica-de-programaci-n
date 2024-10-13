def busqueda_binaria(lista,objetivo):
    """
    Busca un elemento en una lista ordenada y devuelve su indice

    Args:
        lista (list): lista ordenada a buscar
        objetivo: elemento a buscar en la lista

    Returns:
        int: indice del elemento en la lista
    """
    inicio = 0
    fin = len(lista)-1
    
    while inicio <= fin:
        medio = (inicio + fin) //2
        print(f"Lista Actual: {lista[inicio:fin+1]}")
        print(f"Inicio: {inicio}, Fin: {fin}, Medio: {medio}, Valor Medio: {lista[medio]}")
        input("Presiona enter para continuar.....")
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] <objetivo:
            inicio = medio + 1
        else:
            fin = medio -1

numero_ordenados = [ i for i in range(1,21)]

resultado = busqueda_binaria(numero_ordenados,11)

if resultado:
    print("Encontrado ", resultado)
else:
    print("Elemento no encontrado")