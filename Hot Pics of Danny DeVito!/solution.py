def prevent_distractions(txt):
    nope = ('anime', 'meme', 'vine', 'roasts', 'Danny DeVito')
    return 'NO!' if any(i in txt for i in nope) else 'Safe watching!'
