from math import ceil

def encryption(txt):
    txt = ''.join(i for i in txt if not i.isspace())
    root = len(txt)**0.5
    return ' '.join(txt[i::ceil(root)] for i in range(int(root) + 1))
