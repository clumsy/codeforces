n, a = int(input()), [int(i) for i in input().split()]
a.sort()
res, total, cur = 0, sum(a), 0
while res < n:
    cur += a[n - 1 - res]
    res += 1
    if cur > total - cur:
        break
print(res)
