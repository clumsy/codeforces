x1, y1 = (int(i) for i in input().split())
x2, y2 = (int(i) for i in input().split())
res = max(abs(x2 - x1), abs(y2 - y1))
print(res)
