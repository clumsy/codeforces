t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    c, d = c - a, d - b
    a, b, c, d = min(a, b), max(a, b), min(c, d), max(c, d)
    res = "NO" if a < (b - 1) // 2 or c < (d - 1) // 2 else "YES"
    print(res)
