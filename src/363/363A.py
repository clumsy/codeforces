n = input()
res = []
for d in reversed(n):
    d = int(d)
    s = ("-O" if d >= 5 else "O-") + "|" + "O" * (d % 5) + "-" + "O" * (4 - d % 5)
    res.append(s)
res = "\n".join(res)
print(res)
