#Inicilizacion variables

num:int = 0
i:int = 0
c:int = 0
temp:int = 0

c = int(input("Cuantos numeros quiere comparar: "))

for i in range(c):
    num = int(input("Ingrese un numero: "))
    if num == 1000:
        temp +=1
        print(f"El numero {num} es igual que 1000")
    elif num > 1000:
        temp+=1
        print(f"El numero {num} es mayor que 1000")

print(f"El usuario ingreso {c} numeros y solo {temp} son mayores a 1000")





