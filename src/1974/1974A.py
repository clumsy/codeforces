cnt = 5 * 3
t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    d, r = divmod(y, 2)
    res = d + (r > 0)
    x -= d * (cnt - 2 * 4)
    if r > 0:
        x -= cnt - 4
    x = max(x, 0)
    if x > 0:
        res += (x + cnt - 1) // cnt
    print(res)
