t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    res, cnt, mi = 0, 0, float("inf")
    while a:
        cur = a.pop()
        if cur > x:
            res += 1
        else:
            mi = min(mi, cur)
            cnt += 1
            if mi * cnt >= x:
                res += 1
                mi, cnt = float("inf"), 0
    print(res)
