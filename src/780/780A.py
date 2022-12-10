n, s = int(input()), (int(i) for i in input().split())
res, t = 0, set()
for i in s:
    if i in t:
        t.remove(i)
    else:
        t.add(i)
        res = max(res, len(t))
print(res)
