sumaval:float = 0
promval:float = 0

for i in range(0, 10, 1):
    val = float(input("Ingrese un valor: "))
    sumaval = sumaval + val

promval = sumaval / 10

print(f"La suma de los valores es de {sumaval}, y su respectivo promedio es {promval}")