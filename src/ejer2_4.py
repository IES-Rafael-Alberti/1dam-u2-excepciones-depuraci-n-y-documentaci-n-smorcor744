def atgoritmo_burbuja():
    a = [8, 3, 1, 19, 14]
    total = len(a)
    for i in range(0,len(a)):
        for actual in range(0, total - 1):
            siguiente = actual +1
            if a[actual] > a[siguiente]:
                a[siguiente], a[actual] = a[actual], a[siguiente]
    return a


def main():
    a = atgoritmo_burbuja()
    print(a)


if __name__ == "__main__":
    main()


