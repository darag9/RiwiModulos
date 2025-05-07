#inicializacion de variables

base:float = 0
altura:float = 0
area:float = 0
n:int = 0
areaMayor:float = 0

n = int(input("Ingrese cuantos triangulos quiere calcular: "))
for i in range(n):
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = (base*altura)/2
    print(f"El triangulo con base {base} y altura {altura} tiene un area de {area}")
    if area >= 12:
        areaMayor +=1

print(f"De {n} triangulos ingresados solo {areaMayor} tienen un area mayor a 12")