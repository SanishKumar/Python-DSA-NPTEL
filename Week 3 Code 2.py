def splitsum(l):
    p=0
    n=0
    for i in l:
        if i>=0:
            p=p+(i**2)
        else:
            n+=i**3
    return [p,n]
