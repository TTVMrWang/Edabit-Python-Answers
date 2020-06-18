class Minecart:
	def __init__(self, v=0):
		self.v = v

	def add_speed(self, speed):
		self.v = max(0,min(self.v+speed,24))	

def mine_run(tracks):
	cart = Minecart()
	boost = {"-->":8, "<-->":0, "<--":-8, "---":-3}
	for i in range(len(tracks)-1):
		cart.add_speed(boost[tracks[i]])
		if cart.v == 0: return i
	return True
