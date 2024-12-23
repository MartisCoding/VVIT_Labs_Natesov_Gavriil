# Task 1
def greet(name):
    print("Hello, " + name)

def square(number):
    return number * number

def max_of_two(x, y):
    return max(x, y)
# Task 2
def describe_person(name, age=30):
    return f"{name} is {age} years old."

# Task 3
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
