dirs = {
    "N": (0, +1),
    "S": (0, -1),
    "W": (-1, 0),
    "E": (+1, 0),
}
t = int(input())
for k in range(t):
    n, a, b = (int(i) for i in input().split())
    s = input()
    res = "NO"
    x_ = y_ = None
    for i in range(2):
        x = y = 0
        for c in s:
            dx, dy = dirs[c]
            x, y = x + dx, y + dy
            if i == 1:
                xd, xr = divmod(a - x, x_) if x_ else (0, 0)
                yd, yr = divmod(b - y, y_) if y_ else (0, 0)
                xd = xd if x_ else yd
                yd = yd if y_ else xd
                if (
                    xr == yr == 0
                    and x + yd * x_ == a
                    and y + xd * y_ == b
                    and min(xd, yd) >= 0
                ):
                    res = "YES"
                    break
        x_, y_ = x, y
    print(res)
