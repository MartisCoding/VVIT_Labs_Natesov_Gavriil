# Task 1
def enum():
    num = list(range(int(input("Enter a number: ")) + 1))
    print(*num, sep="\n")

# Task 2
def comparator():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num1 > num2:
        print(f"Greatest number is {num1}")
    elif num1 < num2:
        print(f"Greatest number is {num2}")
    else:
        print("Two numbers are equal")

