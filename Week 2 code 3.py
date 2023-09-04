'''
def rotate(l):
    l.append(l[0])
    l.pop(0)
    #return l

def rotatelist(l,n):
    s=0
    while s<n:
        rotate(l)
        s+=1
    return l
print(rotatelist([1,2,3,4,5],12))
  
        
def rotate(l):
    l.append(l[0])
    l.pop(0)

def rotatelist(l,n):
    s=0
    while s<n:
        rotate(l)
        s+=1
    print(l)
rotatelist([1,2,3,4,5],3)
'''

def rotatelist(l, k):
    if k <= 0:
        return l
    k = k % len(l)
    return l[k:] + l[:k]
