def digits(number):
  l = len(str(number))
  return sum([9*(10**x)*(x+1) for x in range(l-1)])+(number-10**(l-1))*l
