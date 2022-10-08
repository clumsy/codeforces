n = int(input())
res = []
for p in range(n // 2, -n // 2, -1):
    p = abs(p)
    res.append("*" * p + "D" * (n - 2 * p) + "*" * p)
res = "\n".join(res)
print(res)
