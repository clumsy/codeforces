l, r, a = (int(i) for i in input().split())
l, r = min(l, r), max(l, r)
d = min(a, r - l)
res = 2 * (l + d + (a - d) // 2)
print(res)
