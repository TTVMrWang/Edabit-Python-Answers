def diamond(carat):
	h = (carat+1)//2
	quarter = [[int(i==j) for j in range(h)] for i in range(h)]
	half = [l[::-1] + l[carat%2:] for l in quarter]
	full = half + half[:-1][::-1]
	return [full, '{} cut'.format('perfect' if carat%2 else 'good')]
