n, s = int(input()), input()
res, u = 0, set()
for c in s:
    if c.isupper():
        u.clear()
    else:
        u.add(c)
    res = max(res, len(u))
print(res)
