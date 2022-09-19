n, m = (int(i) for i in input().split())
s = set(range(1, m + 1))
for _ in range(n):
    x, *y = (int(i) for i in input().split())
    for i in y:
        s.discard(i)
res = "NO" if s else "YES"
print(res)
