#Inicializacion de variables

opc = ""
i:int = 0
c:bool = True
notas:float = []
prom:float = 0
sumaNotas:float = 0
valorEspecifico = 0
temp = 0

#Validacion de notas

while c: 
    notas.append(float(input("Ingrese una nota: ")))
    if notas[i] <= 100 and notas[i] >= 0:
        print(f"Se ingreso la nota {notas[i]} correctamente\n")
        sumaNotas = notas[i] + sumaNotas
        print(sumaNotas)
        if notas[i] >= 70:
            print("Aprovaste!")
        else:
            print("Reprobaste :c\n")
        i = i+1
        opc = input("Desea agregar otra calificacion? (si/no): ")
        if opc == "no":
            break
        elif opc == "si":
            continue
        else:
            print("Error: Opcion no coincide, se cerrara el programa\n")
            break
    else:
        print("Error: No es posible agregar una nota afuera del rango de 0 a 100")
        notas.pop(i)

print(f'''
        La dimension del arreglo es {i}
        El valor de la suma de las notas es {sumaNotas}
        El arreglo esta formado por {notas}
''')

#Resultado del promedio

prom = sumaNotas / i
print(f"El promedio de las notas es {prom}\n")

#Contar calificaciones mayores

valorEspecifico = float(input("Ingrese el valor especifico el cual quiere comparar las notas: \n"))
i = 0
if valorEspecifico >= 0 and valorEspecifico <= 100:
    for i in range(len(notas)):
        if valorEspecifico == notas[i]:
            print(f"El valor {valorEspecifico} es igual al valor {notas[i]} en la posicion del arreglo {i+1}\n")
        elif valorEspecifico > notas[i]:
            print(f"El valor {valorEspecifico} es mayor a la nota {notas[i]} en la posicion del arreglo {i+1}\n")
            temp+=1
        else:
            print(f"El valor {valorEspecifico} NO es mayor a la nota {notas[i]} en la posicion del arreglo {i+1}\n")
else:
    print(f"Error: El rango del valor especifico debe ser menor que 100 y mayor que 0, tu valor {valorEspecifico}")

print(f"La cantidad de calificaciones mayores a {valorEspecifico} son {temp}")

