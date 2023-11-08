def cuenta_atras(n):
    cadena = ""

    while n != 0:  
        cadena += f"{n}, "
        n -= 1

    cadena += str(n)  

    return cadena


def main():
    #preguntamos por el numero y comprobamos que sea in entero
    salir = False
    while not salir:
        try:
            n = int(input("Introduzca un número entero: "))
            salir = True
        except ValueError:
            print("***Error***")
        except Exception:
            print("** Error **")
    
    numero = int(n)
    print(cuenta_atras(numero))

if __name__ == "__main__":
    main()