# Task 1
def print_data_from_file():
    with open("lab3 files/example.txt") as file:
        data = file.read()
        print(data)

def print_data_from_file_by_line():
    with open("lab3 files/example.txt") as file:
        for line in file:
            print(line)


# Task 2
def user_input_in_file():
    with open("lab3 files/user_input.txt", "a") as file:
        inp = input()
        file.write(inp + "\n")

# Task 3
def print_data_from_file_by_line_error_handling():
    try:
        with open("lab3 files/example.txt") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print("File not found")



