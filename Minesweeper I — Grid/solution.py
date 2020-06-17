def num_grid(lst):
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j] == '-':
				lst[i][j] = str(sum(1 for u in range(i-1,i+2) for v in range(j-1,j+2) if 0 <= v < len(lst[i]) and 0 <= u < len(lst) and lst[u][v] == '#'))
	return lst
