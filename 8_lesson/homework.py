from abc import ABC, abstractmethod
import math

class User:

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_attrs(self):
        print(self.__dict__)

    def get_attr(self, attr):
        print(self.__dict__["_User__" + attr])

    def set_attr(self, attr, value):
        self.__dict__["_User__" + attr] = value
        self.get_attr(attr)

user_1 = User("vasil", "vasil@mail.com", "123321")
print(user_1.__dict__)
user_1.get_attrs()
user_1.get_attr("password")
user_1.set_attr("name", "vas")
user_1.get_attrs()

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        print(f"Area = {math.pi * (self.radius ** 2)}")
        
class Rectangle(Shape):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def calculate_area(self):
        print(f"Area = {self.width * self.height}")

class Triangle(Shape):

    def __init__(self, long, high) -> None:
        self.long = long
        self.high = high

    def calculate_area(self):
        print(f"Area = {(self.long * self.high) / 2}")

circle = Circle(15)
circle.calculate_area()
rectangle = Rectangle(5, 6)
rectangle.calculate_area()
triangle = Triangle(6, 10)
triangle.calculate_area()