def all_prime(lst):
	return all(is_prime(i) for i in lst)
	
def is_prime(n):
	return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))
