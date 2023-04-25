n, d = (int(i) for i in input().split())
b = (int(i) for i in input().split())
res = prev = 0
for e in b:
    times = max(0, (prev + 1 - e + d - 1) // d)
    res += times
    prev = e + d * times
print(res)
