n, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res = cur = 0
prv = None
for i in a:
    if i == prv:
        cur = 0
    cur += 1
    res = max(res, cur)
    prv = i
print(res)
