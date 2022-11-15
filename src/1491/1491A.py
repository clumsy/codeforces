n, q = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
o = a.count(1)
for _ in range(q):
    t, v = (int(i) for i in input().split())
    if t == 1:
        o += 1 if a[v - 1] == 0 else -1
        a[v - 1] = 1 - a[v - 1]
    else:
        res = 1 if v <= o else 0
        print(res)
