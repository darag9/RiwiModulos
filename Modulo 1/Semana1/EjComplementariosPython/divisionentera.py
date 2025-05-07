num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))


if num2 == 0:
    print("No es posible dividir un numero entre 0")
else:
    print(f"La division entera es: {num1//num2} y su modulo es: {num1%num2}")