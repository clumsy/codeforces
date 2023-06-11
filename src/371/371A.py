n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res = 0
for j in range(k):
    o = t = 0
    for i in range(n // k):
        w = j + i * k
        o += a[w] == 1
        t += a[w] == 2
    res += min(o, t)
print(res)
