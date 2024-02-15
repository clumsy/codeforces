t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    rs = {}
    for _ in range(n):
        r = [int(i) for i in input().split()]
        rs[r[0]] = r
    for _ in range(m):
        c = [int(i) for i in input().split()]
        if c[0] in rs:
            ord = c
    for i in ord:
        res = rs[i]
        print(*res)
