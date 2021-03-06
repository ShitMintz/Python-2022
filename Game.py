from adventurelib import *


Room.items = Bag()
##########################
#Define Rooms
##########################
space = Room("You are drifting in space and you see an abandoned ship flying around")
cafeteria = Room("You are in a cafeteria with three exits")
weapons = Room("you are in a weapons room with two exits")
hallway1 = Room("you are in a hallway with four exits")
o2 = Room("You are in an O2 room with one exit")
navigation = Room("You are in a navigations room with one exit")
shields = Room("You are in a shields room with two exits")
hallway2 = Room("You are in a hallway with three exits")
communications = Room("You are in a Communications room with one exit")
storage = Room("You are in a storage room with three exits")
hallway3 = Room("You are in a hallway with two exits")
lowerengine = Room("You are in the lower engine room with two exits")
hallway4 = Room("You are in a hallway with four exits")
reactor = Room("You are in a reactor room with one exits")
security = Room("You are in a security room with one exit")
upperengine = Room("You are in the Upper Engine room with two exits")
hallway5 = Room("You are in a hallway with three exits")
medbay = Room("You are in a medbay with one exit")
hallway6 = Room("You are in a hallway with three exits")
admin = Room("You are in an admin room with one exit")
electrical = Room("You are in a room with one exit")
##########################
#Room Connections
##########################
cafeteria.east = weapons
cafeteria.south = hallway6
cafeteria.west = hallway5
hallway5.east = cafeteria
hallway5.south = medbay
hallway5.west = upperengine
medbay.north = hallway5
upperengine.east = hallway5
upperengine.south = hallway4
hallway4.north = upperengine
hallway4.east = security
hallway4.south = lowerengine
hallway4.west = reactor
reactor.east = hallway4
security.west = hallway4
lowerengine.north = hallway4
lowerengine.east = hallway3
hallway3.west = lowerengine
hallway3.north = electrical
hallway3.east = storage
electrical.south = hallway3
storage.west = hallway3
storage.north = hallway6
storage.east = hallway2
hallway6.north = cafeteria
hallway6.east = admin
hallway6.south = storage
admin.west = hallway6
hallway2.west = storage
hallway2.east = shields
hallway2.south = communications
communications.north = hallway2
shields.west = hallway2
shields.north = hallway1
hallway1.north = weapons
hallway1.east = navigation
hallway1.south = shields
hallway1.west = o2
navigation.west = hallway1
o2.east = hallway1
weapons.south = hallway1
weapons.west = cafeteria

#########################
#variables
inventory = Bag()
current_room = space
body_searched = False
used_keycard = False


#Binds
@when("jump")
def jump():
	print("You jump")

@when("enter ship")
@when("enter spaceship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You climb into the spaceship")
		current_room = cafeteria
	else:
		print("There is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#checks if the current room list of exits has 
		#the direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")

@when("look")
def look():
	print(current_room)
	print("There are exits to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		print(t)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")

#itemsItem.description
keycard = Item("A brown keycard","keycard","card","key","brown keycard")
keycard.description = "You look at the keycard and see that it is labelled, Admin"

note = Item("A scribbled note","note","paper","code")
note.description = "You look at the note. The numbers 4,2,6,9 are scribbled with the word navigation at the top"

@when("look at ITEM")
def look(item):
	if item in inventory:
		print(inventory.find(item).description)

#add items to room
o2.items.add(note)
admin.items.add(keycard)

@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("use ITEM")
def use(item):
	if inventory.find(item)==keycard and current_room == admin:
		print("You use the keycard and the escape pod slides open")
		print("The escape pod stands open to the south")
		admin.west = escape
	elif item == "note" and "note" in inventory:
		if current_room == navigation:
			print("You enter the code and the ship starts up. You win")
		else:
			print("There is no where for you to enter the code")
	elif item == "note":
		print("You don't have the code.")

	else:
		print("You can't use that here")



def main():
	print(current_room)
	start()
	#start the main loop

main()