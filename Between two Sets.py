def getTotalX(a, b):
    div=[]
    count=0
    c=0
    for i in range(1,b[0]+1):
        for j in a:
            if i%j==0:
                c=c+1
        if c==len(a):
            div.append(i)
        c=0
    temp=0
    for i in div:
        for j in b:
            if j%i==0:
                temp=temp+1
        if temp==len(b):
            count=count+1
        temp=0
    return(count)
