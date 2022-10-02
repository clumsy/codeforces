a, b = (int(i) for i in input().split())
a, b = min(a, b), max(a, b)
res = (a, (b - a) // 2)
print(*res)
