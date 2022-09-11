n, m = (int(i) for i in input().split())
res = n - 1 if m == 1 else n * (m - 1)
print(res)
