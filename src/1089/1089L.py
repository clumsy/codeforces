n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
order = sorted(range(n), key=b.__getitem__, reverse=True)
taken, res = set(), []
for i in order:
    if a[i] in taken:
        res.append(b[i])
    else:
        taken.add(a[i])
diff = len(taken) - k
res = sum(res[diff:]) if diff < 0 else 0
print(res)
