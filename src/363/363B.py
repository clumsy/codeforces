n, k = (int(i) for i in input().split())
h = [int(i) for i in input().split()]
mi, s, res = float("inf"), 0, 0
for i, e in enumerate(h):
    s += e
    if i >= k:
        s -= h[i - k]
    if i >= k - 1 and s < mi:
        res, mi = i - k + 2, s
print(res)
