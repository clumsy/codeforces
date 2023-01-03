n = int(input())
cols = [0] * n
res = 0


def c2n(k):
    return k * (k - 1) // 2


for _ in range(n):
    rows = 0
    for i, c in enumerate(input()):
        if c == "C":
            rows += 1
            cols[i] += 1
    res += c2n(rows)
for col in cols:
    res += c2n(col)
print(res)
