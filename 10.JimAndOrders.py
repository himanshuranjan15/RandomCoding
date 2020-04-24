def jimOrders(orders,n):
    for i in range(n):
        orders[i]=sum(orders[i])
    g=[]
    for i in sorted(orders):
        if orders.index(i)+1 not in g:
            g.append(orders.index(i)+1)
        else:
            orders[orders.index(i)]=0
            g.append(orders.index(i)+1)
    
    return(g)
