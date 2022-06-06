from class_objs import Car, NewCar, Player


def main():

    Player1 = Player("Player 1")
    Player2 = Player("Player 2")
    while Player1.position < 100 or Player2.position < 100:
        # print("Player 1 start position is at {0}".format(Player1.position))
        Player1.role_dice()
        Player1.check_for_ladders()
        Player1.check_for_snakes()
        Player1.increment_role()
        # print("Player 1 end position is at {0}".format(Player1.position))
        if Player1.position >= 100:
            print("Player 1 Wins on role {0}".format(Player1.role))
            break

        # print("Player 2 start position is at {0}".format(Player2.position))
        Player2.role_dice()
        Player2.check_for_ladders()
        Player2.check_for_snakes()
        Player2.increment_role()
        # print("Player 2 end position is at {0}".format(Player2.position))
        if Player2.position >= 100:
            print("Player 2 Wins on role {0}".format(Player2.role))
            break

    # MyCar = Car("Seat", "Leon")
    # MyCar.first_function()
    # print(MyCar)
    # MyNewCar = NewCar("Scoda", "Octavia")
    # MyNewCar.first_function()


if __name__ == "__main__":
    main()

