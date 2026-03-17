

def calc_area(shape, num1, num2=0):
    if shape == "t":
        print(0.5 * num1 * num2)
    elif shape == "r":
        print(num1 * num2)
    elif shape == "s":
        print(num1 ** 2)
    elif shape == "c":
        print(3.14 * num1 ** 2)

shape = input("Enter shape:")

if shape == "t":
    num1 = int(input("Enter base: "))
    num2 = int(input("Enter height: "))
    calc_area(shape, num1, num2)

elif shape == "r":
    num1 = int(input("Enter width: "))
    num2 = int(input("Enter height: "))
    calc_area(shape, num1, num2)

elif shape == "s":
    num1 = int(input("Enter side: "))
    calc_area("r", num1)

elif shape == "c":
    num1 = int(input("Enter radius: "))
    calc_area(shape, num1)

else:
    print(" not shape")
