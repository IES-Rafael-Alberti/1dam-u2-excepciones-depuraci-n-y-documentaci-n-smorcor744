def atgoritmo_burbuja():
    """
    Esta función implementa el algoritmo de ordenamiento de burbuja.
    Ordena una lista de números en orden ascendente.

    Returns:
        list: La lista de números ordenada en orden ascendente.
    """
    a = [8, 3, 1, 19, 14]
    total = len(a)
    for i in range(0,len(a)):
        for actual in range(0, total - 1):
            siguiente = actual +1
            if a[actual] > a[siguiente]:
                a[siguiente], a[actual] = a[actual], a[siguiente]
    return a


def main():
    """
    Esta es la función principal que se ejecuta cuando se inicia el programa.
    Llama a la función atgoritmo_burbuja y muestra el resultado.
    """
    a = atgoritmo_burbuja()
    print(a)


if __name__ == "__main__":
    """
    Este es el punto de entrada del programa.
    Llama a la función main cuando se ejecuta el script.
    """
    main()