t = int(input())
for _ in range(t):
    r, g, b = sorted(int(i) for i in input().split())
    res = "YES" if b - (r + g) < 2 else "NO"
    print(res)
