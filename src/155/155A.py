n, a = int(input()), (int(i) for i in input().split())
mi = ma = next(a)
res = 0
for i in a:
    if i < mi or i > ma:
        res += 1
        mi, ma = min(i, mi), max(i, ma)
print(res)
