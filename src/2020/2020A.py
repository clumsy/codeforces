t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res, i = 0, 1
    if k > 1:
        while i * k <= n:
            i *= k
    while i > 1:
        if n >= i:
            d = n // i
            res += d
            n -= d * i
        i //= k
    res += n
    print(res)
