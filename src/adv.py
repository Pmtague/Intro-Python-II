from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
"North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare items

item = {
	'candle': Item("candle", "This candle burns bright"),
	'dagger': Item("dagger", "dagger: I will cut you"),
	'tunic': Item("tunic", "The fanciest shirt this side of the foyer"),
	'shoes': Item("shoes", "Shop no further, these kicks aim to please"),
	'map': Item("map", "map: This useless piece of paper will get you nowhere, but it looks cool"),
	'rock': Item("rock", "rock: All the comforts of cave-dwelling"),
	'pants': Item("pants", "pants: Don't leave home without 'em"),
}

# Link items to rooms

room['foyer'].items.append(item['candle'].name)
room['foyer'].items.append(item['map'].name)
room['overlook'].items.append(item['rock'].name)
room['narrow'].items.append(item['dagger'].name)
room['narrow'].items.append(item['tunic'].name)
room['narrow'].items.append(item['shoes'].name)
room['treasure'].items.append(item['pants'].name)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Please enter your name: ")

player = Player(player_name, room['outside'])

# print(player.current_room)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

directions = ["n", "s", "e", "w"]
actions = ["take", "drop"]
check_inventory = ["i", "inventory"]

while True:
	print(f"\n----------------\n\n{player.name} is currently in the {player.current_room.name}.\n{player.current_room.description}\n")

	if len(player.current_room.items) > 0:
		print(f"The following items are in the {player.current_room.name}:")
		for item in player.current_room.items:
			print(f"\t{item}")

	cmd = input("~~> ").lower()

	if cmd in directions:
		player.travel(cmd)

	elif cmd == "q":
		print("Goodbye!")
		exit()
	
	else:
		print("I did not recognize that command")
	
	if cmd in actions:
		if cmd == "take":
			


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.