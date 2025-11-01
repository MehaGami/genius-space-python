class Animal:

    sound_dict = {
        "cow" : "meeeee",
        "tiger" : "rrrrrrrrr",
        "cat" : "mey",
        "default": "Silence",
    }

    def __init__(self, name, species, age,):
        self.name = name
        self.species = species
        self.age = age
        self.sound = Animal.sound_dict.get(self.species, Animal.sound_dict["default"])
    
    def make_sound(self):
        print(self.sound)

cow = Animal("adsa", "cow", "14")

cow.make_sound()

print(cow.__dict__)

dog = Animal("luffy", "dog", "16")

dog.make_sound()

print(dog.__dict__)

class Rectangle: 

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        print(f"Area = {self.width * self.height}")

Rectangle_1 = Rectangle(14, 20)

Rectangle_2= Rectangle(5, 6)

Rectangle_1.calculate_area()
Rectangle_2.calculate_area()