def happyLadybugs(b):
    lady=list(map(str,b))
    space=0
    temp=0
    if "_" not in b:
        for i in set(b):
            if i+i in b:
                temp=1
            else:
                return("NO")
    for i in set(b):
        if i!='_' and b.count(i)%2==1:
            print(b.count(i))
            return("NO")
            temp=1
        else:
            temp=0
    return("YES")
