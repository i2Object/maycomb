class Inventory:
	def __init__(self, maxSlots, isRoom=False):
		self._isRoom = isRoom
		self.maxSlots = maxSlots
		self.inventory = []

	def addItem(self, item):
		if len(self.inventory) < self.maxSlots or self._isRoom:
			self.inventory.append(item)
		else:
			print("You can't carry all that!")
	
	def __contains__(self, item):
		for inventoryItem in self.inventory:
			if item == inventoryItem:
				return True
		return False
	
	def __str__(self):
		ret = "You have:\n" if not self._isRoom else "There is:\n"
		for inventoryItem in self.inventory:
			ret += f'- {"an" if str(inventoryItem)[0].lower() in "aeiou" else "a"} {str(inventoryItem)}'
		return ret

class Item:
	name = "Mysterious Insect"
	description = "It appears you have found a bug."

	def __str__(self):
		return self.name

class WelcomeGuide(Item):
	name = "Welcome Guide"
	description = "Welcome to the Maycomb text-based adventure game!"
	
	def read(self):
		print("WELCOME TO MAYCOMB!")
		print("I can't be bothered to write an intro.")

class Book(Item):
	name = "Book"
	description = "The source of knowledge"
