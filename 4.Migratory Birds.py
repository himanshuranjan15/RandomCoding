def migratoryBirds(arr):
    x=dict([[l,arr.count(l)] for l in set(arr)])
    z=max(x.values())
    y=[]
    for i in x:
        if x[i]==z:
            y.append(i)
    return(min(y))
