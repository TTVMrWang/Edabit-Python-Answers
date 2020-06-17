def extract_primes(num):
  a = []
  b = []
  for i in range(2,num+1):
    for j in range(2,i):
      if i%j==0:
        break
    else:a.append([i]*str(num).count(str(i)))if str(i) in str(num)else False
  for i in a:
    for j in i:
      b.append(j)
  return b
