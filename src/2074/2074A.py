t = int(input())
for _ in range(t):
    l, r, d, u = (int(i) for i in input().split())
    res = "YES" if l == r == d == u else "NO"
    print(res)
