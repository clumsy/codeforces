t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "YES"
    d, p = 1, next(a)
    for i in a:
        if d > 0:
            if i < p:
                d = -1
        elif i > p:
            res = "NO"
        p = i
    print(res)
