n = int(input())
res = 0
for _ in range(n):
    x1, y1, x2, y2 = (int(i) for i in input().split())
    res += (y2 - y1 + 1) * (x2 - x1 + 1)
print(res)
