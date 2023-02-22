t = int(input())
for _ in range(t):
    n = int(input())
    d, r = divmod(n, 2020)
    res = "YES" if max(0, d - r) * 2020 + r * 2021 == n else "NO"
    print(res)
