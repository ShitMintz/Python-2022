from adventurelib import *



##########################
#Define Rooms
##########################
space = Room("You are drifting in space and you see an abandoned ship flying around")
cafeteria = Room("You are in a cafeteria wiht three exits")
weapons = Room("you are in a weapons room with two exits")
hallway1 = Room("you are in a hallway with four exits")
o2 = Room("You are in an O2 room with one exit")
navigation = Room("You are in a navigations room with one exit")
shields = Room("You are in a shields room with two exits")
hallway2 = Room("You are in a hallway with three exits")
communications = Room("You are in a Communications room with one exit")
storage = Room("You are in a storage room with three exits")
hallway3 = Room("You are in a hallway with two exits")
loweregine = Room("You are in the lower engine room with two exits")
hallway4 = Room("You are in a hallway with four exits")
reactor = Room("You are in a reactor room with one exits")
security = Room("You are in a security room with one exit")
upperengine = Room("You are in the Upper Engine room with two exits")
hallway5 = Room("You are in a hallway with three exits")
medbay = Room("You are in a medbay with one exit")
hallway6 = Room("You are in a hallway with three exits")
admin = Room("You are in a room with one exit")

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
hallway4.south = loweregine
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
weapons.east = cafeteria

#########################
#variables
inventory = bag()
current_room = space
body_searched = False
used_keycard = False


#Binds
@when("jump")
def jump():
	print("You jump")

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_airlock():
	global current_room
	if current_room == space:
		print("You haul yourself into the airlock")
		current_room = airlock
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

def main():
	print(current_room)
	start()
	#start the main loop

main()