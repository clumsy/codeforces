n, x, y = (int(i) for i in input().split())
need = (n * y + 99) // 100
res = max(0, need - x)
print(res)
