n, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
ma = 0
for i, e in enumerate(a):
    cur = (e + m - 1) // m
    if cur >= ma:
        res = i + 1
        ma = cur
print(res)
