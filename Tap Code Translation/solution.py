def tap_code(text):
    encrypt = dict(zip('abcdefghijlmnopqrstuvwxyz', ((a, b) for a in range(1, 6) for b in range(1, 6))))
    decrypt = {v: k for k, v in encrypt.items()}

    res = []
    if text[0] != '.':
        for i in text.replace('k', 'c'):
            r, c = encrypt[i]
            res.append('{} {}'.format('.' * r, '.' * c))
        return ' '.join(res)
    else:
        groups = text.split()
        for i in range(0, len(groups), 2):
            res.append(decrypt[(len(groups[i]), len(groups[i+1]))])
        return ''.join(res)
