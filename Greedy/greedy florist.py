def getMinimumCost(k, c):
    cost = 0
    c.sort()
    round = 1
    for _ in range(k):
        cost += c.pop()
        
    while c:
        for _ in range(k):
            if not c:
                break
            else:
                cost = cost + (round + 1)*c.pop()
        round += 1
    print(cost)
