n, m = (int(i) for i in input().split())
a = sum(int(i) for i in input().split())
x = min(n + a, n - a)
res = []
for _ in range(m):
    l, r = (int(i) for i in input().split())
    sz = r - l + 1
    res += [1 if sz & 1 == 0 and sz <= x else 0]
print(*res, sep="\n")
