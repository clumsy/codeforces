t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    next(b)
    res = 0
    for _ in range(n):
        res += max(0, next(a) - next(b, 0))
    print(res)
