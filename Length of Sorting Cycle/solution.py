def cycle_length(lst,n):
    slst = sorted(lst)
    if lst.index(n) == slst.index(n):
        return 0
    else:
        ct = 1
        pos,swap_pos=lst.index(n),slst.index(n)
        lst[pos],lst[swap_pos] = lst[swap_pos],n
        return ct + cycle_length(lst,lst[pos])
