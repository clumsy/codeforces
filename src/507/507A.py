n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
order = sorted(range(n), key=a.__getitem__)
res = []
for i in order:
    k -= a[i]
    if k < 0:
        break
    res.append(i + 1)
print(len(res))
if res:
    print(*res)
