'''
def mystery(l):
  if (l == []):
    return(l)
  else:
    mid = len(l)//2
    if (len(l)%2 == 0):
      return l[mid-1:mid+1] + mystery(l[:mid-1]+l[mid+1:])
    else:
      return l[mid:mid+1] + mystery(l[:mid]+l[mid+1:])
'''

def rainaverage(l):
    l1=[]
    for i in l:
        for 
