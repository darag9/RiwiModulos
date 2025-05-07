def vowels(word:str)->int:
    temp:int = 0
    for i in range(len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            temp += 1
    return temp

def main():
    print(vowels("balatro"))

main()