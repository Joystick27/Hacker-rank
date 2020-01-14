def decentNumber(n):
    a = 0
    b = n
    s = '-1'
    while n >= 3:
        if not n % 3:
            s = '5'*n + '3'*a
            break
        n -= 5
        a += 5
    if a == b:
        s = '3'* a
    print(s)