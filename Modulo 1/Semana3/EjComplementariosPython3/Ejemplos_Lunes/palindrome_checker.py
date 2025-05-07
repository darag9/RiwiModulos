#def palindrome_checker(word:str)->bool:
#    reversed_word:str = ""
#    for i in range(len(word)):
#        reversed_word += word[i]
#    if word == reversed_word:
#        return True
#    else:
#        return False



#def main():
#    print(palindrome_checker("daniel"))

#main(


matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz[1][0])

word:str = "reconocer"

reversed_word:str = ""
for i in range(len(word)):
    reversed_word += word[i]
    if word == reversed_word:
        print(True)
    else:
        print(False)