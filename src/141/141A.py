g, h, p = (input() for _ in range(3))

res = "YES" if sorted(g + h) == sorted(p) else "NO"
print(res)
