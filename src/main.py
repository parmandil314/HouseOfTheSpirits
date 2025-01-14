from commands import get_command, Command
from house import House
from term import clear


def main():
    clear()
    house = House(input("What's your name? "))
    clear()
    while True:
        house.player.current_room.print_desc()
        command: Command = get_command()
        if command.keyword == "quit":
            print("Are you sure you want to quit?")
            if get_command().keyword == "yes":
                clear()
                break
        else:
            command.execute(house)

if __name__ == "__main__":
    main()