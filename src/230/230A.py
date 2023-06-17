s, n = (int(i) for i in input().split())
xy = sorted([[int(i) for i in input().split()] for _ in range(n)])
res = "YES"
for x, y in xy:
    if s <= x:
        res = "NO"
    s += y
print(res)
