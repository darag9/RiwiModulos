diccionario:dict = {
    "valor1":True,
    "valor2":False,
    "valor3":False,
    "valor4":True,
    "valor5":False,
    "valor6":False,
    "valor7":True
}

for value, key in diccionario.items():
    print(value, key)

for value in diccionario:
    if diccionario[value]:
        print(value)