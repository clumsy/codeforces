t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = 0
    for i, e in enumerate(a):
        nr = n // 2 + (n & 1 == 1 and i & 1 == 0)
        res = max(res, e + nr)
    print(res)
