t = int(input())
for _ in range(t):
    x, y = [None] * 3, [None] * 3
    for i in range(3):
        x[i], y[i] = (int(i) for i in input().split())
    dxb, dxc = x[1] - x[0], x[2] - x[0]
    dyb, dyc = y[1] - y[0], y[2] - y[0]
    res = 1  # always together at Alice's
    if dxb * dxc > 0 and dyb * dyc > 0:
        res += min(abs(dxb), abs(dxc)) + min(abs(dyb), abs(dyc))
    elif dxb * dxc > 0:
        res += min(abs(dxb), abs(dxc))
    elif dyb * dyc > 0:
        res += min(abs(dyb), abs(dyc))
    print(res)
