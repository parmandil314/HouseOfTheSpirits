from src.term import clear


def get_command():
    raw_command = input("> ")

    clear()

    finished_command = Command()
    finished_command.args = []

    in_quotes = False
    i = 0
    while len(raw_command) > 0:
        try:
            if raw_command[i] == '"':
                if in_quotes:
                    in_quotes = False
                else:
                    in_quotes = True

            if raw_command[i] == " " and not in_quotes:
                if finished_command.keyword is None:
                    finished_command.keyword = raw_command[0:i]
                    raw_command = raw_command[i+1:]
                else:
                    arg = raw_command[0:i]
                    if arg[0] == '"':
                        arg = arg[1:]
                    if arg[-1] == '"':
                        arg = arg[0:-2]
                    finished_command.args.append(arg)
                    raw_command = raw_command[i+1:]
                i = 0
            elif i == len(raw_command) - 1:
                if finished_command.keyword is None:
                    finished_command.keyword = raw_command
                    raw_command = ""
                else:
                    arg = raw_command
                    if arg[0] == '"':
                        arg = arg[1:]
                    if arg[-1] == '"':
                        arg = arg[0:-1]
                    finished_command.args.append(arg)
                    raw_command = ""
                i = 0
            else:
                i += 1
        except IndexError:
            pass
    return finished_command


class Command:
    def __init__(self, keyword: str = None, args: list = ()):
        self.keyword = keyword
        self.args = args

    def execute(self, house):
        if self.keyword == "go":
            if int(self.args[0]) <= len(house.player.current_room.adjoining_rooms):
                house.player.current_room = house.rooms[house.player.current_room.adjoining_rooms[int(self.args[0]) - 1]]
            else:
                print(f"You can't get to that room directly from {house.player.current_room.name}")
        elif self.keyword == "talk":
            house.player.talk(self.args[0])
        else:
            print("Command not understood.")