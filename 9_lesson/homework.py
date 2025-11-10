from abc import ABC, abstractmethod
from math import pi
class User:

    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password

class UserManager():

    def __init__(self) -> None:
        self.users_list = []

    def get_users_data(self):
        print("----------------start------------")
        for user in self.users_list:
            print(user.__dict__)
        print("----------------end------------")

    def create_user(self, name, email, password):
        user = User(name, email, password)
        self.users_list.append(user)
        return self.users_list
    
    def delete_user(self, name):
        for index, user in enumerate(self.users_list):
            if user.name == name:
                remove_index = index
                break
        self.users_list.pop(remove_index)
        return self.users_list
    
    def change_user_attr(self, name, password, attr, value):
        for user in self.users_list:
            if user.name == name and user.password == password:
                setattr(user, attr, value)

user_manager = UserManager()
user_manager.create_user("vasyl", "vasil@mail.com", "123")
user_manager.create_user("van", "van@mail.com", "123")
user_manager.create_user("petro", "petro@mail.com", "123")
user_manager.get_users_data()
user_manager.delete_user("vasyl")
user_manager.get_users_data()
user_manager.change_user_attr("van", "123", "email", "vanoger@mail.com")
user_manager.get_users_data()

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)
        
class Rectangle(Shape):

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class CalcuteArea():

    @staticmethod
    def calculate(shape: Shape):
        return shape.calculate_area()
    
class PrintArea():

    @staticmethod
    def print(calculate: CalcuteArea, shape: Shape):
        print(f"Area: {calculate.calculate(shape)}")

calculate_area = CalcuteArea()
print_area = PrintArea()
circle = Circle(15)
print_area.print(calculate_area, circle)
rectangle = Rectangle(5, 6)
print_area.print(calculate_area, rectangle)

class IPrint(ABC):

    @abstractmethod
    def print(self):
        pass

class ICopy(ABC):

    @abstractmethod
    def copy(self):
        pass

class IScan(ABC):

    @abstractmethod
    def scan(self):
        pass

class NetworkPrinter(IPrint, ICopy, IScan):

    def scan(self):
        print("scaning . .. . ..  .. . .")

    def copy(self):
        print("copy . .. . ..  .. . .")

    def print(self):
        print("printing somthing . .. . ..  .. . .")

class Printer(IPrint):

    def print(self):
        print("printing somthing . .. . ..  .. . .")

class Scanner(IScan):

    def scan(self):
        print("scaning . .. . ..  .. . .")

print("----------------------------")
scanner = Scanner()
scanner.scan()
print("----------------------------")
printer = Printer()
printer.print()
print("----------------------------")
network_printer = NetworkPrinter()
network_printer.copy()
network_printer.print()
network_printer.scan()
print("----------------------------")


