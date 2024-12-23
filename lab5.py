# Task 1
class Book:
    def __init__(self, title:str, author:str, year:int):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

# Task 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

# Task 3

class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand