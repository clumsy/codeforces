from math import inf

n, x = int(input()), sorted(int(i) for i in input().split())
res = [None] * n
for i in range(n):
    mi = min(x[i] - x[i - 1] if i > 0 else inf, x[i + 1] - x[i] if i < n - 1 else inf)
    ma = max(x[i] - x[0], x[n - 1] - x[i])
    res = mi, ma
    print(*res)
