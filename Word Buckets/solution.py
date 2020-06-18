def split_into_buckets(phrase, n):
    buckets = []
    s = ''
    
    for i in phrase.split():
        if len(i) > n:
            return []
        elif len(s + i) <= n - 1:
            s = (s + ' ' + i).lstrip()
        else:
            if s:
                buckets.append(s)
            s = i
            
    return buckets + [s]
