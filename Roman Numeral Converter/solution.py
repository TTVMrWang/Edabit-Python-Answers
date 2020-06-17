def convert_to_roman(n):
	rom = ['M','D','C','L','X','V','I']
	ara = [1000,500,100,50,10,5,1]
	r = ''
	for i in ara:
		if n//i:
			if n//i!=4:
				r+=(rom[ara.index(i)])*(n//i)
			elif rom[ara.index(i)-1] not in r:
				r+=rom[ara.index(i)]+rom[ara.index(i)-1]
			else:
				r=r[:-1]+rom[ara.index(i)]+rom[ara.index(i)-2]
			n%=i
	return r
