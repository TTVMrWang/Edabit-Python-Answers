def missing_num(lst):
	n = len(lst)
	total = (n + 1) * (n + 2) / 2
	s = sum(lst)
	return total - s
