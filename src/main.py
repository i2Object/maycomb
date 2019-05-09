# Maycomb Text Adventure
from items import *

DIFFICULTY_VALUES = {
	0: {
		"startingHealth": 100,
		"maxHealth": 100,
		"inventoryMaxSlots": 20
	}, 1: {
		"startingHealth": 64,
		"maxHealth": 60,
		"inventoryMaxSlots": 16
	}, 2: {
		"startingHealth": 25,
		"maxHealth": 45,
		"inventoryMaxSlots": 7
	}
}


class Player:
	def __init__(self, name, difficulty):
		self.name = name
		self.health = DIFFICULTY_VALUES[difficulty]["startingHealth"]
		self.maxHealth = DIFFICULTY_VALUES[difficulty]["maxHealth"]
		self.score = 0
		self.inventory = Inventory(DIFFICULTY_VALUES[difficulty]["inventoryMaxSlots"])
		

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.items = Inventory(0, isRoom=True)
		self.exits = {}
	

class Map:
	def __init__(self, initialRoom):
		self.currentRoom = initialRoom
		self.rooms = {self.currentRoom.name: self.currentRoom}
	
	def describeSurroundings(self):
		print(f"""{self.currentRoom.name} \n {self.currentRoom.description} \n {str(self.currentRoom.items)}""")

	def go(self, direction):
		if direction in self.currentRoom.exits:
			self.currentRoom = self.currentRoom.exits[direction]
		else:
			print("You can't go that way.")
	
	def __getitem__(self, roomName):
		return self.rooms[roomName]
	
	def addRoom(self, room):
		self.rooms[room.name] = room


player = Player("Theo", 0)
player.inventory.addItem(WelcomeGuide())
map = Map(Room("Scout's Bedroom", "You are in your bedroom. To the north is a door leading out of your room into the hallway."))
map.addRoom(Room("Hallway", "The Finch house hallway."))
map["Scout's Bedroom"].exits["north"] = map["Hallway"]
map["Hallway"].exits["south"] = map["Scout's Bedroom"]
map.currentRoom.items.addItem(Book())

while True:
	print()
	map.describeSurroundings()
	action = input("> ").lower()
	if action.startswith("say"):
		print(f"\"{action[4:].capitalize()}\", you say to yourself. Your resolve is greatly strengthened.")
	elif action.startswith("go"):
		map.go(action[3:].lower())
	else:
		print("I don't understand.")

"""
Send to
Louise
Jacques
Isi
Tsuf
Sarah
"""
