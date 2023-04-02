t = int(input())
for _ in range(t):
    x, n, m = (int(i) for i in input().split())
    while n > 0:
        h = x // 2 + 10
        if h >= x:
            break
        else:
            x = h
        n -= 1
    res = "YES" if x - 10 * m <= 0 else "NO"
    print(res)
