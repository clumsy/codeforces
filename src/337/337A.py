n, m = (int(i) for i in input().split())
f = sorted(int(i) for i in input().split())
res = f[n - 1] - f[0]
for i in range(n, m):
    res = min(res, f[i] - f[i - n + 1])
print(res)
