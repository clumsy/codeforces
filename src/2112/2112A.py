t = int(input())
for _ in range(t):
    a, x, y = (int(i) for i in input().split())
    dx, dy = abs(a - x), abs(a - y)
    res = "NO" if dx + dy == abs(y - x) else "YES"
    print(res)
