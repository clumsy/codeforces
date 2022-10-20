n = int(input())
a, b = [0, 0], [0, 0]
for _ in range(n):
    t, x, y = (int(i) for i in input().split())
    z = a if t == 1 else b
    z[0] += x
    z[1] += y
for z in [a, b]:
    res = "LIVE" if 2 * z[0] >= sum(z) else "DEAD"
    print(res)
