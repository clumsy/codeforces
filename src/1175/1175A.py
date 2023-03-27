t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = 0
    while n > 0:
        d, r = divmod(n, k)
        res += r + (d > 0)
        n = d
    print(res)
