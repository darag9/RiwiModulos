def calculadora():
    print("1. suma")
    print("2. Resta")
    opcion = int(input("Elige una opcion (1/2): "))
    
    if opcion > 2 or opcion < 1:
        print("Error")
    else:
        num1 = float(input("primer numero: "))
        num2 = float(input("Segundo numero: "))

    if opcion == 1:
        print(f"Resultado {num1 + num2}")
    elif opcion == 2:
        print(f"Resultado: {num1-num2}")
    

calculadora()