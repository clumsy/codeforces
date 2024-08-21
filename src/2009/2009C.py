t = int(input())
for i in range(t):
    x, y, d = (int(i) for i in input().split())
    dx, dy = (x + d - 1) // d, (y + d - 1) // d
    res = 2 * dy if dy >= dx else 2 * dx - 1
    print(res)
