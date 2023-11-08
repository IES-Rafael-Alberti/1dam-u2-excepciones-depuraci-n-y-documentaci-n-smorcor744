def pedirNum():
    salir = False
    while not salir:
        try:
            entrada = int(input("Introduzca un número entero: "))
            salir = True
        except ValueError as e:
            print("La entrada no es correcta "+ str(e))
        except Exception:
            print("** Error **")
    
    edad = int(entrada)

    return edad

def main():
    pedirNum()



if __name__ == "__main__":
    main()