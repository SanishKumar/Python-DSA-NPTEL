def remdup(l):
    l1=[]
    for i in range (len(l)-1,-1,-1):
        if l[i] in l1:
            continue
        else:
            l1.append(l[i])
        #l1.reverse()
    return (list(reversed(l1)))
