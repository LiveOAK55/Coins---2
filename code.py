def check(n, w, d, m):
    sm = 0
    for i in range(1, n):
        sm += (i * w)
    res = abs((m - sm)//d)
    if sm == m:
        res = n
    return res
    
