from class_objs import Car, NewCar


def main():
    MyCar = Car("Seat", "Leon")
    MyCar.first_function()
    print(MyCar)
    MyNewCar = NewCar("Scoda", "Octavia")
    MyNewCar.first_function()


if __name__ == "__main__":
    main()

