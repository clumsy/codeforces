t = int(input())
for _ in range(t):
    n, c = int(input()), (int(i) for i in input().split())
    cur = next(c)
    res = max(0, cur - 1)
    for i in c:
        if i > cur:
            res += i - cur
        cur = i
    print(res)
