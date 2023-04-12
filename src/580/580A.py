n, a = int(input()), (int(i) for i in input().split())
res = cur = prev = 0
for i in a:
    if i < prev:
        cur = 0
    cur += 1
    prev = i
    res = max(res, cur)
print(res)
