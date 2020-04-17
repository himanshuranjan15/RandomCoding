def birthday(s, d, m):
    count=0
    for i in range(len(s)-m+1):
        D=0
        for j in range(m):
            D=D+s[i+j]
        if D==d:
            count=count+1
    return(candles)
