# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description

		self.n_to = None
		self.s_to = None
		self.e_to = None
		self.w_to = None
		self.items = []

	# def __str__(self):
	# 	return f"\n-----------------\n\n{self.name}\n\n{self.description}\n"
	
	def get_room_in_direction(self, direction):
		if direction == "n":
			return self.n_to
		elif direction == "s":
			return self.s_to
		elif direction == "e":
			return self.e_to
		elif direction == "w":
			return self.w_to
		else:
			return None

	def get_exits(self):
		exits = []
		if self.n_to:
			exits.append("n")
		elif self.s_to:
			exits.append("s")
		elif self.e_to:
			exits.append("e")
		elif self.w_to:
			exits.append("w")
		return exits

	def get_exits_string(self):
		return f"Exits: {', '.join(self.get_exits())}"