t = int(input())
for _ in range(t):
    n, r, b = (int(i) for i in input().split())
    d, m = divmod(r, b + 1)
    res = ("R" * (d + 1) + "B") * m + ("R" * d + "B") * (b - m) + "R" * d
    print(res)
