def cavityMap(grid,n):
    temp=[]
    for  i in range(n):
        d=str(grid.pop(i))
        d=list(map(str,d))
        d=[int(j) for j in d]
        grid.insert(i,d)
    
    for i in  range(1,n-1):
        temp=grid[i]
        d=[]
        for j in range(1,n-1):
            if temp[j]>temp[j-1] and temp[j]>temp[j+1] and temp[j]> grid[i-1][j] and temp[j]>grid[i+1][j]:
                temp[j]=9999
        grid[i]=temp
    z='9999'
    for i in range(n):
        
        grid[i]=[str(j) for j in grid[i]]
        for k in grid[i]:
            if k==z:
                grid[i][grid[i].index(k)]='X'
        grid[i]=''.join(grid[i])
            
    return(grid)
