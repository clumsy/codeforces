n, a, b = (int(i) for i in input().split())
c = [int(i) for i in input().split()]
res = 0
for i in range((n + 1) // 2):
    mi, ma = sorted([c[i], c[n - 1 - i]])
    if ma < 2:
        if mi != ma:
            res = -1
            break
    else:
        res += (
            (2 if i != n - 1 - i else 1) * min(a, b) if mi == 2 else a if mi == 0 else b
        )
print(res)
