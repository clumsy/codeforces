x, y, z, t1, t2, t3 = (int(i) for i in input().split())
res = "YES" if (abs(z - x) + abs(y - x)) * t2 + 3 * t3 <= abs(y - x) * t1 else "NO"
print(res)
