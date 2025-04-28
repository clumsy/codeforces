t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    k = s.count(">")
    lo = hi = n - k
    res = [lo]
    for i, c in enumerate(s):
        if c == ">":
            hi += 1
            res.append(hi)
        else:
            lo -= 1
            res.append(lo)
    print(*res)
