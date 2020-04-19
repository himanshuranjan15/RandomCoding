def pageCount(n, p):
    turn=0
    z=[[i,i+1] for i in range(0,n+1,2)]
    if n-p<=p-1:
        z.reverse()
    for i in z:
        if p in i:
            return(turn)
        turn=turn+1
