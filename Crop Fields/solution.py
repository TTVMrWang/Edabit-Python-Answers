def crop_hydrated(field):
	for y in range(len(field)):
		for x in range(len(field[y])):
			if not watered(field,y,x):
				return False
	return True
	
def watered(lst, y, x):
	if lst[y][x] == 'w':
		return True
	if y > 0:
		if lst[y-1][x] == 'w':
			return True
		if x > 0 and lst[y-1][x-1] == 'w':
			return True
		if x < len(lst[0])-1 and lst[y-1][x+1] == 'w':
			return True
	if y < len(lst)-1:
		if lst[y+1][x] == 'w':
			return True
		if x > 0 and lst[y+1][x-1] == 'w':
			return True
		if x < len(lst[0])-1 and lst[y+1][x+1] == 'w':
			return True
	if x > 0 and lst[y][x-1] == 'w':
		return True
	if x < len(lst[0])-1 and lst[y][x+1] == 'w':
		return True
	return False
