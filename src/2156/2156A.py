t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    while n > 2:
        d = n // 3
        res += d
        n -= 2 * d
    print(res)
