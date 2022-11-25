n, m = (int(i) for i in input().split())
res = []
w, s = "#" * m, "." * (m - 1) + "#"
for r in range(n):
    if r & 1 == 0:
        res.append(w)
    else:
        res.append(s)
        s = s[::-1]
res = "\n".join(res)
print(res)
