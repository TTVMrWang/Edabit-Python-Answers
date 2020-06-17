import textwrap
def ascending(s):
    for i in range(1,round(len(s)/2)+1):
        x = [int (j) for j in textwrap.wrap(s,i)]
        y= [x[0]+k*1 for k in range(len(x))]
        if x==y:
            return True
    return False
