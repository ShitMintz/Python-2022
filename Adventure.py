#import all the functions from adventurelib
from adventurelib import *

#rooms
space = Room("you are drifting in space. you see a spaceship")
airlock = Room("you are in an airlock")
cargo = Room("you are in the cargo bay")
docking = Room("you are in the docking bay")
hallway = Room("you are in the hallway with four exits")
bridge = Room("you stand on the bridge of the ship. There is a dead body")
mess = Room("you are in the kitchen/dining area")
quarters = Room("you are in the crew quarters. There is a locker")
escape = Room("You are in an escape pod")

#variables
current_room = space


#binds
@when("jump")
def jump():
	print("you jump")

@when("enter airlock")
@when("enter spaceship")
@when ("enter ship")
def enter_airlock():
	global current_room
	if 
	current_room == space:
		print("you haul yourself into the airlock")
		current_room = enter_airlock
	else:
		print("there is no airlock here")
	print(current_room)

@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}")
		print(current_room)
	else:
		print("you can't go that way")*

@when("look")
def look():
	print("look around")
#everyting goes above here - do not change
#anything below this line
#the main function
def main():
	print(current_room)
	start()
	#start the main loop

main()