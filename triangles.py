print("Input lengths of the triangle sides: ")
x = int(input("Length of a: "))
y = int(input("Length of b: "))
z = int(input("Length of c: "))

try:
    if isinstance(x and y and z, int):    
        if x == y or x == z or y == z:
            if x == y and x == z:
                print("Equilateral")
            else:
                print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Input has to be an integer")
except ValueError:
    print("Wops")


