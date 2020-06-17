def tournament_scores(gmz):
    tdata = {}
    for gm in gmz:
        t1, s1, _, s2, t2 = gm.split()
        s1, s2 = map(int, (s1, s2))
        for t, s1, s2 in ((t1, s1, s2),(t2, s2, s1)):
            pts = 3 if s1 > s2 else 1 if s1 == s2 else 0
            if t in tdata:
                tdata[t] = (tdata[t][0]+pts, tdata[t][1]+s1, tdata[t][2]+s1-s2)
            else:
                tdata[t] = (pts, s1, s1-s2)
    return sorted([[k, v[0], v[1], v[2]] for k,v in tdata.items()], key=lambda x: x[1:], reverse=1)
