t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    # the onle case for NO is if it's non-increasing
    # first we need n moves, then n - 1, ..., 1 = (n - 1)*n/2
    res, ma = "NO", next(a)
    for i in a:
        if i >= ma:
            res = "YES"
            break
        ma = i
    print(res)
