n, a = int(input()), (int(i) for i in input().split())
res, prev = [], 0
for i, e in enumerate(a):
    if i > 0 and e == 1:
        res.append(i - prev)
        prev = i
res.append(n - prev)
print(len(res))
print(*res)
