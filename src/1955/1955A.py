t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    d, r = divmod(n, 2)
    res = min(2 * a, b) * d + a * r
    print(res)
