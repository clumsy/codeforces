t = int(input())
for _ in range(t):
    x, y, n = (int(i) for i in input().split())
    d, r = divmod(n, x)
    res = x * (d if r >= y else d - 1) + y
    print(res)
