#Declaracion variables

x:float = 0
y:float = 0
n:int = 0
c1:int = 0
c2:int = 0
c3:int = 0
c4:int = 0

n = int(input(("Ingrese cuantos puntos quiere procesar: ")))

for i in range(n):
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))
    if x > 0 and y > 0:
        print(f"Las coordenadas {x,y} se encuentran en el cuadrante 1")
        c1+=1
    elif x < 0 and y > 0:
        print(f"Las coordenadas {x,y} se encuentran en el cuadrante 2")
        c2+=1
    elif x < 0 and y < 0:
        print(f"Las coordenadas {x,y} se encuentran en el cuadrante 3")
        c3+=1
    elif x > 0 and y < 0:
        print(f"Las coordenadas {x,y} se encuentran en el cuadrante 4")
        c4+=1
    else:
        print("No es posible ingresar un valor 0")

print(f'''
    La cantidad de coordenadas en el cuadrante 1 son: {c1}
    La cantidad de coordenadas en el cuadrante 2 son: {c2}
    La cantidad de coordenadas en el cuadrante 3 son: {c3}
    La cantidad de coordenadas en el cuadrante 4 son: {c4}
''')