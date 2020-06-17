def first_and_last(s):
  x = ''.join(sorted(list(s)))
  return [x, x[::-1]]
