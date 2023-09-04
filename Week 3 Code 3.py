def matrixflip(myl,x):
    if x=='h':
        l1=[]
        for i in myl:
            l1.append(list(reversed(i)))
        return l1
    elif x=='v':
        return list(reversed(myl))
    else:
        return myl
                
