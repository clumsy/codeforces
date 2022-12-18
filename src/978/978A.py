n, a = int(input()), [int(i) for i in input().split()]
res, uniq = [], set()
for i in reversed(a):
    if i not in uniq:
        uniq.add(i)
        res.append(i)
print(len(res))
res = reversed(res)
print(*res)
