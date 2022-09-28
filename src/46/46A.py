n = int(input())
res, cur = [], 1
for i in range(n - 1):
    cur = 1 + (cur + i) % n
    res.append(cur)
print(*res)
