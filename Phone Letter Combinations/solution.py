from itertools import product

def letter_combinations(digits):
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
         '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    return [''.join(p) for p in product(*[d[i] for i in digits])]
