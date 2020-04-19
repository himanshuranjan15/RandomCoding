def jumpingOnClouds(c,n):
    jump=0
    current=0
    while(current<n-1):
        if c[current+1]==0 and current+1!=n-1:
            if c[current+2]==0:
                current=current+2
                jump=jump+1
            else:
                current=current+1
                jump=jump+1
        else:
            current=current+2
            jump=jump+1
    return(jump)
