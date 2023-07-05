n, k = (int(i) for i in input().split())
a = sorted(int(i) for i in input().split())
res, cum = [], 0
for i in range(n):
    if k == len(res):
        break
    a[i] -= cum
    if a[i] > 0:
        res.append(a[i])
        cum += a[i]
res += [0] * (k - len(res))
print(*res, sep="\n")
