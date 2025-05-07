def bigger_number(number_1:int, number_2:int, number_3:int)->int:
    bigger:int = 0
    if number_1 > number_2 and number_1 > number_3:
        bigger = number_1
        return bigger
    elif number_2 > number_1 and number_2 > number_3:
        bigger = number_2
        return bigger
    elif number_3 > number_2 and number_3 > number_1:
        bigger = number_3
        return bigger
    else:
        return bigger
    
    
def main():
    print(bigger_number(15,9,38))

main()