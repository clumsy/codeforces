t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    rs, cs = [0] * n, [0] * m
    for r in range(n):
        s = input()
        for c, e in enumerate(s):
            cs[c] += e == "1"
            rs[r] += e == "1"
    rs, cs = sum(r & 1 for r in rs), sum(c & 1 for c in cs)
    res = rs + cs - min(rs, cs)
    print(res)
