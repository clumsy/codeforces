x, y, z = (int(i) for i in input().split())
a, b, c = (int(i) for i in input().split())
res = "YES" if a >= x and a + b - x >= y and a + b + c - x - y >= z else "NO"
print(res)
