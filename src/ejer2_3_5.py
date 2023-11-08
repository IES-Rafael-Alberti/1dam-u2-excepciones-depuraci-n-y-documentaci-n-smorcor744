def contraseña():
    pasware = "usuario"
    pas = input("Introduzca la contraseña: ")
    if pas != pasware:
        raise NameError("Incorrect Password!!")
    
    try:
        contraseña()
    except NameError as e:
        print("error" + e)


contraseña()



