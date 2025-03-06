t = int(input())
for _ in range(t):
    n, k, p = (int(i) for i in input().split())
    d, r = divmod(abs(k), p)
    d += r > 0
    res = -1 if d > n else d
    print(res)
