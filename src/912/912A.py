a, b = (int(i) for i in input().split())
x, y, z = (int(i) for i in input().split())
res = max(0, 3 * z + y - b) + max(0, 2 * x + y - a)
print(res)
