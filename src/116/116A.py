n = int(input())
res, cur = 0, 0
for _ in range(n):
    a, b = (int(i) for i in input().split())
    cur += b - a
    res = max(res, cur)
print(res)
