t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "NO"
    o, p = 0, None
    for i, e in enumerate(a):
        o += e == 1
        if i and e == p == 0:
            res = "YES"
        p = e
    res = "YES" if o == n else res
    print(res)
