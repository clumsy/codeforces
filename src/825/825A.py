n, s = int(input()), input()
res = [0]
for c in s:
    if c == "0":
        res.append(0)
    else:
        res[-1] += 1
res = "".join(str(i) for i in res)
print(res)
