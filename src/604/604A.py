x = [500, 1000, 1500, 2000, 2500]
m = (int(i) for i in input().split())
w = (int(i) for i in input().split())
h = [int(i) for i in input().split()]
res = (
    100 * h[0]
    - 50 * h[1]
    + sum(
        max(int(0.3 * xi), int(xi * (250 - mi) // 250 - 50 * wi))
        for xi, mi, wi in zip(x, m, w)
    )
)
print(res)
