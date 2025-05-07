for i in range(3):
    password:str = input("Ingrese la contraseña: ")
    if password == "python123":
        print("Acceso permitido")
        break
    else:
        print(f"Contraseña incorrecta le quedan {2-i} intentos")
