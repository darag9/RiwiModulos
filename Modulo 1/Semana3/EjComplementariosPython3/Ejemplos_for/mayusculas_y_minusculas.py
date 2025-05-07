palabra:str = input("Ingrese una palabra: ")
temp_mayuscula:int = 0
temp_minuscula:int = 0

for i in range(len(palabra)):
    if palabra[i].isupper():
        print(f"mayuscula: {palabra[i]}")
        temp_mayuscula += 1
    else:
        print(f"minuscula: {palabra[i]}")
        temp_minuscula += 1

print(f"La palabra {palabra} tiene {temp_mayuscula} mayusculas y {temp_minuscula} misnusculas")