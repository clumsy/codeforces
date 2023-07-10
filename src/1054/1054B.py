n, a = int(input()), (int(i) for i in input().split())
res = ma = -1
for i, e in enumerate(a):
    if e > ma + 1:
        res = i + 1
        break
    ma = max(ma, e)
print(res)
