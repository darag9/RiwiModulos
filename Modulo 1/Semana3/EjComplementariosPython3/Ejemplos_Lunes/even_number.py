def is_pair(number:int)->bool:
    if number % 2 == 0:
        return True
    else:
        return False
    
def main():
    print(is_pair(5))

main()