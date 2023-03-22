n, d = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res, prev = 0, None
for i, e in enumerate(a):
    if n == 1 or i % (n - 1) == 0:
        res += 1 + (n == 1)  # can always build one to the left or right
    if i > 0:
        res += e - d >= prev + d
        res += prev + d < e - d
    prev = e
print(res)
