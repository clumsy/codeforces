n, m, a, b = (int(i) for i in input().split())
free = n % m
res = min(free * b, (m - free) * a)
print(res)
