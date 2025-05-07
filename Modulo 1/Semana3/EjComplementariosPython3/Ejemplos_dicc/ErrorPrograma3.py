dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
llaves1 = dic1.keys()
valores1 = dic1.values()

print(llaves1)
print(valores1)

dic2.update(dic1)
print(dic2)

