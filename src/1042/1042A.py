n, m = (int(input()) for _ in range(2))
b = [int(input()) for _ in range(n)]
ma = max(b)
mi = max(ma, (sum(b) + m + n - 1) // n)
ma = ma + m
res = mi, ma
print(*res)
