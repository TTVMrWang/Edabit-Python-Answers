def hex_lattice(n):
	n = (3 + (12 * n - 3) ** .5) / 6
	if n % 1: return "Invalid"
	n = int(n)
	R = list(range(n, 2 * n))
	return '\n'.join((i * 'o ').center(4 * n - 1) for i in R + R[-2::-1])
