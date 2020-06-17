def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if not n%i:
            return False
    return True

def truncatable(n):
    s = str(n)
    if '0' in s:
        return False
    
    left = all(is_prime(int(s[-i:])) for i in range(1, len(s) + 1))
    right = all(is_prime(int(s[:i])) for i in range(1, len(s) + 1))

    return {(True, False): 'left', (False, True): 'right', 
            (True, True): 'both'}.get((left, right), False)
