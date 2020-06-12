def equal_slices(total, people, each):
	if people == 0:
		return True
	if people * each <= total:
		return True
	else:
		return False
