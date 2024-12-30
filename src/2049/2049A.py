t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    p = None
    res = cur = 0
    for i in a:
        if i != 0 and p == 0:
            res += cur > 0
            cur = 0
        cur += i != 0
        p = i
    res += cur > 0
    res = min(res, 2)
    print(res)
