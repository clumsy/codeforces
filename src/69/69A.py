n = int(input())
res = xs = ys = zs = 0
for _ in range(n):
    x, y, z = (int(i) for i in input().split())
    xs += x
    ys += y
    zs += z
res = "YES" if xs == 0 and ys == 0 and zs == 0 else "NO"
print(res)
