#Inicializacion de variables

n1:float = 0
n2:float = 0
n3:float = 0
prom:float = 0
texto1:str = "Promovido"
texto2:str = "Regular"
texto3:str = "Reprobado"

#Declaracion de variables por el usuario

n1, n2, n3 = (float(input("Ingrese una nota: ")), float(input("Ingrese otra nota: ")), float(input("Ingrese otra nota: ")))

#Flujo logico

prom = (n1+n2+n3)/3

if prom > 7:
    print(f"{texto1} con promedio {prom}")
elif prom >= 4 and prom < 7:
    print(f"{texto2} con promedio {prom}")
else:
    print(f"{texto3} con promedio {prom}")
