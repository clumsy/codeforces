n, res = int(input()), 0
for _ in range(n):
    x, y = (int(i) for i in input().split())
    res = max(res, x + y)
print(res)
