n, k = (int(i) for i in input().split())
a, res = ord("a"), []
for i in range(n):
    res.append(chr(a + (i % k)))
res = "".join(res)
print(res)
