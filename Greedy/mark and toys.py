def maximumToys(prices, k):
    prices.sort(reverse = True)
    s = 0
    while prices:
        if k < prices[-1]:
            break
        k -= prices.pop()
        s += 1
    return str(s)