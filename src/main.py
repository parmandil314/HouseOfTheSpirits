from src.house import House
from src.commands import get_command, Command
from src.term import clear

def display_help():
    clear()
    print("Welcome to the interactive game of The House of the Spirits!")
    print("To move to an adjoining room, input 'go' and then the room number.")
    print("To talk to someone, input 'talk', a space, and the name of the character.")
    print("Not all characters are available, or interested in talking to you.")
    print("They will be described, but not listed by name.")
    print("When you input a 'talk' command, an interface will open up for you to")
    print("communicate with the chosen character. You can choose from a")
    print("list of one or more things to say to a character by simply inputting")
    print("the number that corresponds with the desired list item.")
    print("Press the Enter key once you have read this help message.")
    input()
    clear()

def main():
    display_help()
    name = input("What's your name?\n> ")
    version = 0
    while version not in [1, 2]:
        version = int(input("Which version of the house do you want to visit?\n1\n2\n> "))
        if version not in [1, 2]:
            print("Invalid version.")
    house = House(name, version)

    clear()
    while True:
        house.player.current_room.print_desc()
        command: Command = get_command()
        if command.keyword == "quit":
            print("Are you sure you want to quit?")
            word = get_command().keyword
            if word == "yes" or word == "y":
                clear()
                break
        else:
            try:
                command.execute(house)
            except ValueError:
                print("Invalid command. Try again.")

if __name__ == "__main__":
    main()