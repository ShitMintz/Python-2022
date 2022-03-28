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
