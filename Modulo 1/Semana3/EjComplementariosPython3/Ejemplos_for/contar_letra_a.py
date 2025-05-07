palabra:str = input("Ingrese una palabra: ")
temp:int = 0
for i in palabra:
    if i == "a":
        temp += 1

print(f"Su palabra tiene {temp} letras a")