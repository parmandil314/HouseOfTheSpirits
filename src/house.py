from typing import List

from src.dialogue import dialogue_map, run_dialogue
from src.term import clear


class Character:
    def __init__(self, name: str, current_room):
        self.name = name
        self.desc = ""
        self.current_room = current_room
        self.dialogue = dialogue_map[self.name]

esteban = Character(
    "Esteban",
    "Hall"
)

clara = Character(
    "Clara",
    "Unused Rooms"
)

blanca = Character(
    "Blanca",
    "Library"
)

jaime = Character(
    "Jaime",
    "Jaime's Room"
)

nicolas = Character(
    "Nicolas",
    "Dining Room"
)

class Room:
    def __init__(self, house, characters: List[Character], name: str, desc: str, *adjoining_rooms):
        self.house = house
        self.name = name
        self.desc = desc
        self.adjoining_rooms: List[str] = adjoining_rooms
        self.characters = characters

    def print_desc(self):
        clear()
        print(f"You're in the {self.name}. {self.desc}")
        if len(self.characters) == 0:
            print("There are no characters in this room.")
        elif len(self.characters) > 1:
            print(f"There are {len(self.characters)} characters in this room:")
            for i in self.characters:
                print(f"   {i.name}")
        else:
            print("There is one character in this room:")
            print(f"   {self.characters[0].name}")
        print(f"From here you can get to:")
        for i, room in enumerate(self.adjoining_rooms):
            print(f"   {i+1}: {room}")

class Player:
    def __init__(self, name: str, current_room: Room):
        self.name = name
        self.current_room = current_room
        self.known_names = []

    def talk(self, char_name: str):
        for i in self.current_room.characters:
            if char_name == i.name:
                run_dialogue(self, i)

class House:
    def __init__(self, player_name: str = "Player", version: int = 1):
        if version == 1:
            self.rooms = {
                "Dining Room": Room(
                    self,
                    [],
                    "Dining Room",
                    "It's a large room with a beautiful table as its centerpiece.",
                    "Hall", "Kitchen"
                ),
                "Living Room": Room(
                    self,
                    [],
                    "Living Room",
                    "It's a comfortable room with expensive furniture, including a sofa, several armchairs, a piano, and many bookcases.",
                    "Hall"
                ),
                "Hall" : Room(
                    self,
                    [],
                    "Hall",
                    "It's a spacious room with many doors leading to other areas of the house.",
                    "Living Room", "Study", "Library", "Master Bedroom", "Unused Rooms", "Basement", "Kitchen", "Stairs", "Dining Room"
                ),
                "Study": Room(
                    self,
                    [esteban],
                    "Study",
                    "It's a medium-sized room, dominated by a large mahogany desk, and adorned with Persian carpets and fancy bookcases. A tall, somewhat intimidating man is sitting at the desk, operating a typewriter.",
                    "Hall", "Library"
                ),
                "Library": Room(
                    self,
                    [blanca],
                    "Library",
                    "It's a lofty room covered with bookshelves on all sides. A small girl is sitting on a couch, reading an enormous leather-bound book.",
                    "Study", "Hall"
                ),
                "Master Bedroom": Room(
                    self,
                    [],
                    "Master Bedroom",
                    "It's large for a bedroom, with an ornate bed and a small three-legged table in one corner.",
                    "Hall"
                ),
                "Unused Rooms": Room(
                    self,
                    [clara],
                    "Unused Rooms",
                    "This series of mostly unused rooms is dusty and less effectively maintained than the others. In one particularly empty pantry, a woman is in the process of dealing out a complicated spread of tarot cards.",
                    "Hall"
                ),
                "Basement": Room(
                    self,
                    [],
                    "Basement",
                    "A very large animal skin is rolled up in one corner of this basement. The rest is full of boxes, mostly of useless trinkets, as well as a few sets of fine jewelry.",
                    "Hall"
                ),
                "Kitchen": Room(
                    self,
                    [],
                    "Kitchen",
                    "This spotlessly maintained kitchen is occupied by a number of servants, who are working frantically to fabricate a decadent meal. They are overseen by a woman who is herself working hard cleaning up spills and other messes even as they are made.",
                    "Hall", "Dining Room"
                ),
                "Stairs": Room(
                    self,
                    [],
                    "Stairs",
                    "This staircase leads up to a small hallway with doors leading onto unused rooms.",
                    "Hall", "Attics"
                ),
                "Attics": Room(
                    self,
                    [],
                    "Attics",
                    "These three rooms are used as storage spaces now, but they look like they could easily be repurposed as living spaces.",
                    "Stairs"
                )
            }
        elif version == 2:
            self.rooms = {
                "Dining Room": Room(
                    self,
                    [nicolas],
                    "Dining Room",
                    "It's a large room with a once-magnificent table that is currently being used for what appears to be a class in flamenco dancing, led by a handsome young man and attended by a number of young women.",
                    "Hall", "Kitchen"
                ),
                "Living Room": Room(
                    self,
                    [],
                    "Living Room",
                    "It's a comfortable room with expensive furniture, including a sofa, several armchairs, a piano, and many bookcases.",
                    "Hall"
                ),
                "Hall": Room(
                    self,
                    [],
                    "Hall",
                    "It's a spacious room with many doors leading to other areas of the house.",
                    "Living Room", "Study", "Library", "Master Bedroom", "Unused Rooms", "Basement", "Kitchen", "Stairs", "Dining Room"
                ),
                "Study": Room(
                    self,
                    [],
                    "Study",
                    "It's a medium-sized room, dominated by a large mahogany desk, and adorned with Persian carpets and fancy bookcases. A note lies on the desk next to a typewriter. It reads, 'I'm currently out delivering a speech. If you aren't listening to the official Conservative news channel, you should go home and do so now. I'll be back at 2:00.'",
                    "Hall", "Library"
                ),
                "Library": Room(
                    self,
                    [],
                    "Library",
                    "It's a lofty room covered with bookshelves on all sides.",
                    "Study", "Hall"
                ),
                "Master Bedroom": Room(
                    self,
                    [],
                    "Master Bedroom",
                    "It's large for a bedroom, with an ornate bed and a small three-legged table in one corner.",
                    "Hall"
                ),
                "Unused Rooms": Room(
                    self,
                    [],
                    "Unused Rooms",
                    "This series of mostly unused rooms is dusty and less effectively maintained than the others.",
                    "Hall"
                ),
                "Basement": Room(
                    self,
                    [],
                    "Basement",
                    "A very large animal skin is rolled up in one corner of this basement. The rest is full of boxes, mostly of useless trinkets, as well as a few sets of fine jewelry.",
                    "Hall"
                ),
                "Kitchen": Room(
                    self,
                    [],
                    "Kitchen",
                    "This room is occupied by a number of servants, who are working frantically to fabricate a decadent meal. They don't seem to have any direction other than a recipe scribbled on a badly stained piece of paper, and are making messes left and right.",
                    "Hall", "Kitchen", "Dining Room"
                ),
                "Stairs": Room(
                    self,
                    [],
                    "Stairs",
                    "This staircase leads up to a small hallway with doors leading onto unused rooms.",
                    "Hall", "Jaime's Room", "Nicolas' Room"
                ),
                "Jaime's Room": Room(
                    self,
                    [jaime],
                    "Jaime's Room",
                    "This closet-like room holds a small army cot, a small cabinet, and a small desk which highlight the massive towers of textbooks which are also present. A young man sits at the desk, bent over a handwritten essay.",
                    "Stairs"
                ),
                "Nicolas' Room": Room(
                    self,
                    [],
                    "Nicolas' Room",
                    "This medium-sized room holds a bed and a few cabinets and wardrobes, which contain various philosophical works, and a few",
                    "Stairs"
                )
            }
        self.player = Player(player_name, self.rooms["Hall"])