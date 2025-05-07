num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 == num2:
    print(f"{num1} es igual que {num2}")
else:
    print(f"{num1} es menor que {num2}")