def farey(n):
	s = {}
	for denum in range(1, n + 1):
		for num in range(denum + 1):
			k = num / denum
			if k not in s:
				s[k] = '{}/{}'.format(num, denum)
	return [s[v] for v in sorted(s.keys())]
