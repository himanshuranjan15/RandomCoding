def balancedSums(arr):
    Sum=sum(arr)
    count=0
    for i in range(n):
        if Sum-arr[i]-count==count or Sum-arr[i]==0:
            return("YES")
        count=count+arr[i]
    return("NO")
