n, a = int(input()), (int(i) for i in input().split())
res = cur = 0
for i, e in enumerate(a):
    if cur == i:
        res += 1
    cur = max(cur, e)
print(res)
