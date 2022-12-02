n, s = int(input()), input()
res = []
i, d = 0, 1
while i < n:
    res.append(s[i])
    i += d
    d += 1
res = "".join(res)
print(res)
