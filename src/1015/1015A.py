n, m = (int(i) for i in input().split())
seg = []
for _ in range(n):
    l, r = (int(i) for i in input().split())
    seg.append((l, +1))
    seg.append((r, -1))
seg.sort()
res, c, prev = [], 0, 0
for p, d in seg:
    if c == 0:
        res.extend(range(prev + 1, p))
    c += d
    prev = p
res.extend(range(prev + 1, m + 1))
print(len(res))
print(*res)
