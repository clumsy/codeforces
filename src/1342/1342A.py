t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    x, y = sorted([x, y])
    a, b = (int(i) for i in input().split())
    res = min(a * (x + y), b * x + a * (y - x))
    print(res)
