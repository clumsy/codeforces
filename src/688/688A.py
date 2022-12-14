n, d = (int(i) for i in input().split())
res, cur = 0, 0
for _ in range(d):
    p = sum(int(i) for i in input())
    if p < n:
        cur += 1
    else:
        cur = 0
    res = max(res, cur)
print(res)
