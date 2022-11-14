k, s = int(input()), input()
res, k = [], 0
for c in s:
    if c == "B":
        k += 1
    elif k > 0:
        res.append(k)
        k = 0
if k > 0:
    res.append(k)
print(len(res))
if res:
    print(*res)
