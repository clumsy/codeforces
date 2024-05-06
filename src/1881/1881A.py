t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    x, s = (input() for _ in range(2))
    res, cur = -1, 0
    while True:
        if s in x:
            res = cur
            break
        if cur > 1 and n > m:
            break
        x += x
        n *= 2
        cur += 1
    print(res)
