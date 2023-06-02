t = int(input())
for _ in range(t):
    c, s = (int(i) for i in input().split())
    d, r = divmod(s, c)
    res = r * (d + 1) ** 2 + (c - r) * d**2
    print(res)
