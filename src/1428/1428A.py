t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = (int(i) for i in input().split())
    res = abs(x1 - x2) + abs(y1 - y2) + (0 if x1 == x2 or y1 == y2 else 2)
    print(res)
