def binary_clock(time):
    digits = [list('{:0>4b}'.format(int(i))) for i in time.replace(':', '')]
    clock = [list(i) for i in zip(*digits)]
    for r, c in ((0, 0), (0, 2), (0, 4), (1, 0)):
        clock[r][c] = ' '
    clock = [''.join(i) for i in clock]
    return clock
