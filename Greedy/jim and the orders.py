def jimOrders(orders):
    order = list()
    for i in range(len(orders)):
        order.append([i, orders[i][0]+orders[i][1]])
    order.sort(key=lambda a: a[1])
    l = [a[0]+1 for a in order]
    return l