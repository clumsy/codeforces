t = int(input())
for _ in range(t):
    n = int(input())
    a, b, c = (input() for _ in range(3))
    res = not all(z == x or z == y for x, y, z in zip(a, b, c))
    res = "YES" if res else "NO"
    print(res)
