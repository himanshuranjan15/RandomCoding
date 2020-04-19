def stones(n, a, b):
    stone=[]
    diff=abs(a-b)
    first=min(a,b)*(n-1)
    stone.append(first)
    for i in range(n-1):
        first=first+diff
        stone.append(first)
    print(stone)
    sto=list(dict.fromkeys(stone)) #creating orderd set using dictionary
    return(sto)
