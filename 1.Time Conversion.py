#https://www.hackerrank.com/challenges/time-conversion/problem

n= list(map(str,input().split(':')))
def timeConversion(n):
    if 'AM' in n[2]:
        n[2]=n[2].strip('AM')
        n=[int(i) for i in n]
        if n[0]==12:
            n[0]=n[0]-12

    else:
        n[2]=n[2].strip('PM')
        n=[int(i) for i in n]
        if n[0]==12:
            n[0]=n[0]
        else:
            n[0]=n[0]+12
    for i in range(len(n)):
        if n[i]<10:
            n[i]='0'+str(n[i])
        else:
            n[i]=str(n[i])
    v=":".join(n)
    return(v)
x=timeConversion(n)
print(x)
