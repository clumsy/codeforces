t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    res = "YES" if len({a, b, c, d}) == 1 else "NO"
    print(res)
