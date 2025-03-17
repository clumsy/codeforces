t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = [-1] * n
    for p in range(n):
        a = (int(i) for i in input().split())
        s = set(i % n for i in a)
        if len(s) == 1:
            [k] = s
            if res[k] < 0:
                res[k] = p + 1
    res = [-1] if -1 in res else res
    print(*res)
