def numero_impar(n):
    #Creamos una cadena vacia y una variable para ir de impar en impar
    cont = 1
    cadena = ""
    #mientras la variable sea menor que el numero que nos a dado
    while cont < n:  
        cadena += f"{cont}, "
        cont += 2
        #le suma a la cadena la variable y despues pasa al siguiente impar
    #le sumamos el numero que nos a dado
    cadena += str(n)  
    return cadena


def main():
    #preguntamos por el numero y comprobamos que sea in entero
    salir = False
    while not salir:
        try:
            n = int(input("Introduzca un númweo entero: "))
            salir = True
        except ValueError:
            print("***Error***")
        except Exception:
            print("** Error **")
    
    numero = int(n)
    print(numero_impar(numero))

if __name__ == "__main__":
    main()