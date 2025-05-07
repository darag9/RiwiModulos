pi: float = 3.1416

def circle_area(radius:float)->float:
    result = pi * radius ** 2
    return result

def main():
    print(circle_area(8))

main()