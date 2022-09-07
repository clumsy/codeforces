y, b, r = (int(i) for i in input().split())
x = min(y, b - 1, r - 2)
res = x + (x + 1) + (x + 2)
print(res)
