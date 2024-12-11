t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res, cur = float("inf"), 0
    for e, i in sorted((-e, i) for i, e in enumerate(a)):
        res = min(res, i + cur)
        cur += 1
    print(res)
