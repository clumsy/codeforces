a = sorted(int(i) for i in input().split())
s = sum(a)
res = "YES" if s == 2 * sum(a[:3]) or s == 2 * sum(a[1:3]) else "NO"
print(res)
