n, a = int(input()), (int(i) for i in input().split())
res, r = 1, 0
for i in a:
    k = 1
    while i % (k * 2) == 0:
        k *= 2
    if i % k == 0:
        if k > res:
            r = 1
        elif k == res:
            r += 1
        res = max(res, k)
print(res, r)
