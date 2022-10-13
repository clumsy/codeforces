n, k = (int(i) for i in input().split())
res = []
for i in range(n):
    row = [0] * n
    row[i] = k
    res.append(row)
res = "\n".join(" ".join(str(c) for c in r) for r in res)
print(res)
