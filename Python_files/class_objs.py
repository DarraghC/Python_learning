from dataclasses import dataclass


@dataclass
class Car:
    make: str
    model: str
    # def __init__(self, make, model):
    #     self.make = make
    #     self.model = model

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


