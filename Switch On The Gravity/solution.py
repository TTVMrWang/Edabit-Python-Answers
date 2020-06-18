def switch_gravity_on(lst):
    W, H = len(lst[0]), len(lst)
    L = [list(i) for i in zip(*lst)]
    for i in range(W):
        row = L[i]
        L[i] = ['-'] * (H - row.count('#')) + ['#'] * row.count('#')
    return [list(i) for i in zip(*L)]
