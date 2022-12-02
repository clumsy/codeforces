n, m = (int(i) for i in input().split())
res = [n // m] * m
for i in range(n % m):
    res[i] += 1
print(*res)
