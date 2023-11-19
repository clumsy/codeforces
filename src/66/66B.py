n, h = int(input()), (int(i) for i in input().split())
res = s = nxt = 0
prv = d = -1
for i, e in enumerate(h):
    if e > prv:
        if d < 0:
            d = 1
            s = nxt
    elif e < prv:
        if d > 0:
            d = -1
        nxt = i
    prv = e
    res = max(res, i - s + 1)
print(res)
