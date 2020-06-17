def polybius(text):
    coords = [str(i) + str(j) for i in range(1, 6) for j in range(1, 6)]
    encrypt = dict(zip('abcdefghiklmnopqrstuvwxyz', coords))
    decrypt = dict(zip(coords, 'abcdefghiklmnopqrstuvwxyz'))
    
    if text[0].isalpha():
        text = ''.join(i for i in text.lower() if i.isalpha() or i == ' ')
        return text.replace('j', 'i').translate(str.maketrans(encrypt))
    else:
        res = []
        for word in text.split():
            res.append(''.join(decrypt[word[i:i+2]] for i in range(0, len(word), 2)))
        return ' '.join(res)
