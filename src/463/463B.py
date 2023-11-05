n, h = int(input()), (int(i) for i in input().split())
res = e = p = 0
for i in h:
    res += max(0, (i - p) - e)
    e = max(0, e - (i - p))
    p = i
print(res)
