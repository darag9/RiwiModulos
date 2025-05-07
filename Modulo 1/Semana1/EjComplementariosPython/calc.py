num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))

print('''
      1. Suma
      2. Resta
      3. Multiplicacion
      4. Division

      Ingrese una opcion.
''')

opc = int(input())

if opc == 1:
    print(f"{num1} + {num2} = {num1+num2}")
elif opc == 2:
    print(f"{num1} - { num2} = {num1-num2}")
elif opc == 3:
    print(f"{num1} * {num2} = {num1*num2}")
elif opc == 4:
    print(f"{num1} / {num2} = {num1/num2}")
else:
    print("Opcion no encontrada")