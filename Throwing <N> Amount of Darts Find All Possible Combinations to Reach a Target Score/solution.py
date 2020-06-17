from itertools import combinations_with_replacement as cwr

def darts_solver(sections, darts, target):
	results = [i for i in cwr(sections, darts) if sum(i) == target]
	return ['-'.join(map(str, i)) for i in results]
