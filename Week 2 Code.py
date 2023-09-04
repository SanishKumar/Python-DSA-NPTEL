#m=int(input())
def prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True


def primepartition(m):
    
    if m<=0:
        return False
    else:
        for i in range(2,m+1):
            if prime(m-i) and prime(i):
                return True
        return False

#print(primepartition(m))


'''
def rotate(l):
    l.append(l[0])
    l.pop(0)

def rotatelist(l,n):
    s=0
    while s<n:
        rotate(l)
        s+=1
    print(l)
#rotatelist([1,2,3,4,5],3)
'''

def rotatelist(l, k):
    if k <= 0:
        return l
    k = k % len(l)
    return l[k:] + l[:k]

