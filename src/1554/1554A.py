t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    res, x = 0, next(a)
    for y in a:
        res, x = max(res, x * y), y
    print(res)
