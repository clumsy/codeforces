t = int(input())
for _ in range(t):
    x1, y1 = (int(i) for i in input().split())
    x2, y2 = (int(i) for i in input().split())
    x3, y3 = (int(i) for i in input().split())
    res = 0
    if y1 == y2 and y3 < y1:
        res = abs(x1 - x2)
    elif y2 == y3 and y1 < y2:
        res = abs(x2 - x3)
    elif y3 == y1 and y2 < y3:
        res = abs(x3 - x1)
    print(res)
