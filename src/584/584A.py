n, t = (int(i) for i in input().split())
res = t
while len(str(res)) < n:
    res *= t
res = res if len(str(res)) == n else -1
print(res)
