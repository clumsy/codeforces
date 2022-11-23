n = int(input())
res, i = [], 0
while 1 << i <= n:
    if n & (1 << i) != 0:
        res.append(i + 1)
    i += 1
res = reversed(res)
print(*res)
