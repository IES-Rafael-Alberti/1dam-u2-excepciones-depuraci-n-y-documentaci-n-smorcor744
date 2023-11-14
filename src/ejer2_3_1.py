def pedirEdad():
    salir = False
    while not salir:
        try:
            entrada = int(input("Introduzca su edad: "))
            salir = True
        except ValueError:
            print("***Error*** edad introducida no válida.")
        except Exception:
            print("** Error **")
    
    edad = int(entrada)

    return edad


def mayorEdad(edad):
    for i in range(1,edad):
        print(i)
    print(edad, "\n Has cumplido todos estos años a lo largo de tu vida.")



def main():
    edad = pedirEdad()

    mayorEdad(edad)

if __name__ == "__main__":
    main()