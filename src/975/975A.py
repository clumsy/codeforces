n, s = int(input()), input().split()
res = set()
for w in s:
    c = "".join(sorted(set(i for i in w)))
    res.add(c)
res = len(res)
print(res)
