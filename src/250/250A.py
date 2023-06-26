n, a = int(input()), (int(i) for i in input().split())
res, cnt = [], 0
for i, e in enumerate(a):
    if e < 0:
        cnt += 1
    if cnt == 3:
        res.append(i)
        cnt = 1
res.append(n)
res = [res[i] - (res[i - 1] if i > 0 else 0) for i in range(len(res))]
print(len(res))
print(*res)
