from dataclasses import dataclass
from random import randint

# @dataclass
class Car:
    # make: str
    # model: str
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def first_function(self):
        print("My car is a {0} {1}".format(self.make, self.model))

    # def __str__(self) -> str:
    #     return f"{self.make}, {self.model}"


class NewCar(Car):
    pass
#     def __init__(self, fuel_milage),
#         self.fuel_milage = fuel_milage

#     def fuel_milage_check(self):
#         print("It gets {0} miles per liter".format(self.fuel_milage))

# MyNewCar = NewCar("Scoda", "Octavia")
# MyNewCar.first_function()


class Player:

    def __init__(self, name):
        self.name = name
        self.position = 0
        self.role = 0
        self.ladders_dict = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}
        self.snakes_dict = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}

    def role_dice(self):
        if self.position < 100:
            role = randint(0, 6)
            self.position += role

    def check_for_snakes(self):
        # print("Checking for Snakes")
        for start_pos, end_pos in self.snakes_dict.items():
            if start_pos == self.position:
                self.position = end_pos
                print("Snakes!!!!")

    def check_for_ladders(self):
        # print("Checking for Ladders")
        for start_pos, end_pos in self.ladders_dict.items():
            if start_pos == self.position:
                self.position = end_pos
                print("Ladders!!!!!!")

    def increment_role(self):
        self.role += 1
        # print("{0} is on role {1}".format(self.name, self.role))

