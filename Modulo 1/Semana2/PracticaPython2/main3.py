#Inicializacion de variables

cadenaNotas:str = ""
cadenaIterable:str = ""
suma:float = 0
promedio:float = 0
nota:float = 0
listaNotas:list[float] = []
numNotas:int = 0
notaComparar:float = 0
temp:int = 0

#Ingreso de la cadena y pasarla a una lista de numeros reales

cadenaNotas = input("Ingrese las calificaciones: ")

coma = cadenaNotas[-1]

if coma != ",":
    cadenaNotas = cadenaNotas + ","

for i in cadenaNotas:
    if i != ",":
        cadenaIterable = cadenaIterable.__add__(i)
    else:
        nota = float(cadenaIterable)
        listaNotas.append(nota)
        suma += nota #la suma de las notas para mas adelante sacar el promedio
        cadenaIterable = ""
        numNotas += 1 #el contador de notas para el promedio


#Comparar la nota con las notas de la lista e imprimir que notas de la lista son mayores que la nota comparada

notaComparar = float(input("Ingrese la nota que quiere comparar con las anteriormente agregadas: "))

for x in range(numNotas):
    if notaComparar < listaNotas[x]:
        temp += 1
        print(f"La nota: {listaNotas[x]} es mayor a la nota comparada {notaComparar}")
    
print(f"\nLa cantidad de notas mayores a la nota comparada son: {temp}")

#Promedio y resultado si aprobo o reprobo

promedio = suma/numNotas
if promedio >= 70:
    print(f'''
        Felicidades! aprobaste con un promedio de: {promedio}
    ''')
else:
    print(f"Lo siento :c reprobaste con una nota de: {promedio}")

#Verficiar y contar calificaciones especificas

temp = 0
for k in range(numNotas):
    if notaComparar == listaNotas[k]:
        temp += 1
        print(f"Se encontro la nota {notaComparar} en la posicion {k} del arreglo")
        
print(f"La nota {notaComparar} se encontro un total de {temp} veces")

print(listaNotas)