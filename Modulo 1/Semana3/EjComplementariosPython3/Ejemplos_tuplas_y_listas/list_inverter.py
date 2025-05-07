list1:list = [10,20,30,40]
reverted_list:list = []

for i in range(len(list1)-1, -1, -1):
    reverted_list.append(list1[i])

print(list1)
print(reverted_list)
