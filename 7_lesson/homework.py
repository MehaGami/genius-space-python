class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Your vehicle make {self.make}, model {self.model}, year {self.year}")

class Car(Vehicle):

    def __init__(self, make, model, year, fuel) -> None:
        super().__init__(make, model, year)
        self.fuel = fuel

    def start_engine(self):
        print("brbrbrbrbrbbrbrbbrbrbr")
        print(f"Your {self.model} start")
        if self.fuel <= 10:
            print(f"You need refuel your car, you have {self.fuel} fuel(")
        else:
            print(f"You have {self.fuel} fuel")

    def display_info(self):
        super().display_info()
        print(f"Fuel: {self.fuel}")

class Bicycle(Vehicle):

    def __init__(self, make, model, year, count_of_speeds) -> None:
        super().__init__(make, model, year)
        self.count_of_speeds = count_of_speeds

    def start_going(self):
        print(f"You start go on your {self.model}")
        print(f"You have {self.count_of_speeds} count of speeds")

    def display_info(self):
        super().display_info()
        print(f"Count of speeds: {self.count_of_speeds}")

car_1 = Car("Ford", "car", 2003, 30)
bicycle_1 = Bicycle("Soshimi", "bicycle", 2015, 21)

car_1.start_engine()
print(car_1.__dict__)
print("-----------------")
bicycle_1.start_going()
print(bicycle_1.__dict__)
print("-----------------")
car_1.display_info()
print("-----------------")
bicycle_1.display_info()