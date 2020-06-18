def bar_chart(results):
    def to_bar(q, v):
        return '{}|{}{}{}'.format(q, '#'*(v//50), ' '*(v>0), v)
    _sorted = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(to_bar(q,v) for q,v in _sorted)
