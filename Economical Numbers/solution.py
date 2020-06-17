def is_economical(n):
	l = len(str(n))
	i = 2
	p = count = 0
	while p or n > 1:
		if n % i:
			count += len(str(i)) * (p > 0) + len(str(p)) * (p > 1)
			i += 1
			p = 0
		else:
			n //= i
			p += 1
	if count < l: return 'Frugal'
	if count > l: return 'Wasteful'
	return 'Equidigital'
