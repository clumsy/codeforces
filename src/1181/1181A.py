x, y, z = (int(i) for i in input().split())
res = (x + y) // z, (min(z - x % z, z - y % z) if (x + y) // z > x // z + y // z else 0)
print(*res)
