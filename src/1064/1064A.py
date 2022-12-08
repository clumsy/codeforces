a, b, c = sorted(int(i) for i in input().split())
res = max(0, c - (a + b - 1))
print(res)
