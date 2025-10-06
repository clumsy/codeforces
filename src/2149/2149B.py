t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = p = 0
    for i, e in enumerate(sorted(a)):
        if i & 1 == 0:
            p = e
        else:
            res = max(res, e - p)
    print(res)
