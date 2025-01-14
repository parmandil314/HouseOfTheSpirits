from typing import List

from dialogue import dialogue_map
from term import clear


class Room:
    def __init__(self, house, name: str, desc: str, *adjoining_rooms):
        self.house = house
        self.name = name
        self.desc = desc
        self.adjoining_rooms: List[str] = adjoining_rooms
        self.characters: List[Character]

    def print_desc(self):
        clear()
        print(f"You're in the {self.name}. {self.desc}")
        print(f"From here you can get to:")
        for i in self.adjoining_rooms:
            print(f"   the {self.house.rooms[i].name}")

class Character:
     def __init__(self, name: str, current_room: Room):
         self.name = name
         self.current_room = current_room
         self.dialogue = dialogue_map[self.name]

class Player:
    def __init__(self, name: str, current_room: Room):
        self.name = name
        self.current_room = current_room

class House:
    def __init__(self, player_name: str = "Player"):
        self.rooms = {
            "Living Room": Room(
                self,
                "Living Room",
                "It's a comfortable room with expensive furniture, including a sofa, several armchairs, and many bookcases.",
                "Hall"
            ),
            "Hall" : Room(
                self,
                "Hall",
                "It's a spacious room with many doors leading to other areas of the house.",
                "Living Room", "Study", "Library"
            ),
            "Study": Room(
                self,
                "Study",
                "It's a medium-sized room, dominated by a large mahogany desk, and adorned with Persian carpets and fancy bookcases",
                "Hall", "Library"
            ),
            "Library": Room(
                self,
                "Library",
                "It's a lofty room covered with bookshelves on all sides.",
                "Study", "Hall"
            )
        }
        self.player = Player(player_name, self.rooms["Hall"])