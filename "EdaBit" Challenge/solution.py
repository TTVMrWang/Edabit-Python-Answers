def eda_bit(start, end):
	lst = []
	for x in range(start, end+1):
		if x%3 == 0 and x%5 == 0: lst.append('EdaBit')
		elif x%3 == 0: lst.append('Eda')
		elif x%5 == 0: lst.append('Bit')
		else: lst.append(x)
	return lst
