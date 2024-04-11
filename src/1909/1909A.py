t = int(input())
for _ in range(t):
    n = int(input())
    xp = xn = yp = yn = False
    for _ in range(n):
        x, y = (int(i) for i in input().split())
        if x > 0:
            xp = True
        elif x < 0:
            xn = True
        if y > 0:
            yp = True
        elif y < 0:
            yn = True
    res = "NO" if xp and xn and yp and yn else "YES"
    print(res)
