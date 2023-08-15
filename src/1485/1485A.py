from math import inf

t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    if b > a:
        res = 1
    elif b == a:
        res = 2
    else:
        res = inf
        for i in range(b == 1, 20):
            cur, x = i, a
            while x:
                x //= b + i
                cur += 1
            res = min(res, cur)
    print(res)
