n, m = (int(i) for i in input().split())
x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = (int(i) for i in input().split())
res, cur = "NO", 0
order = sorted(range(n), key=x.__getitem__)
for i in order:
    if x[i] > cur:
        break
    if x[i] <= m <= y[i]:
        res = "YES"
        break
    cur = max(cur, y[i])
print(res)
