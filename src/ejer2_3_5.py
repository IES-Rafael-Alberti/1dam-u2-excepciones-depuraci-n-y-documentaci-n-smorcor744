def contraseña():
    pasware = "usuario"
    pas = input("Introduzca la contraseña: ")
    if pas != pasware:
        raise NameError("Incorrect Password!!")
    else:
        print("Contraseña correcta")

def main():
    try:
        contraseña()
    except NameError as e:
        print("**Error** " + str(e))


if __name__ == "__main__":
    main()

