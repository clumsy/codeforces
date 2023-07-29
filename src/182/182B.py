d, n, a = int(input()), int(input()), (int(i) for i in input().split())
res, cur = 0, d
for i in a:
    res += d - cur if cur <= d else d + 1 - cur
    cur = i
print(res)
