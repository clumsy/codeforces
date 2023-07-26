n, m = (int(i) for i in input().split())
n *= 4
res = (
    i
    for i1, i2 in zip(range(n // 2 + 1, n + 1), range(1, n // 2 + 1))
    for i in (i1, i2)
    if i <= m
)
print(*res)
