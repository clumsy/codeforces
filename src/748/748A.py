n, m, k = (int(i) for i in input().split())
res = (
    (k + 2 * m - 1) // (2 * m),
    ((k - 1) % (2 * m)) // 2 + 1,
    "L" if k & 1 == 1 else "R",
)
print(*res)
