def BinaryS(l):
    s=int(input())
    n=len(l)//2
    if s!=n or s<n :
        n//=2
        elif s>n:
            l=l[n:]
            n=len(l)//2
