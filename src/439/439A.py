n, d = (int(i) for i in input().split())
t = (int(i) for i in input().split())
res = 2 * (n - 1)
d -= sum(t) + 5 * res
res = -1 if d < 0 else res + d // 5
print(res)
