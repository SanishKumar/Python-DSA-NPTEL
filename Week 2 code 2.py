def matched(string):
    i=0
    s=0
    while i<len(string) and s>=0:
        if string[i]=="(":
            s+=1
        elif string[i]== ")":
            s-=1
        i+=1
    if s==0:
        return True
    else:
        return False
print(matched("a)*(asddf"))
            
