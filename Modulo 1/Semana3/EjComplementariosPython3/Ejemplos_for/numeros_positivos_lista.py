lista:list[int] = [3, -1, 5, -2, 7, -8]

i:int = 0

for i in range(len(lista)):
    if lista[i] > 0:
        print(lista[i])