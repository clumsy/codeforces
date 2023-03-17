n, l, r = (int(i) for i in input().split())
mi = 2**l - 1 + (n - l) * 1
ma = 2**r - 1 + (n - r) * (2 ** (r - 1))
res = mi, ma
print(*res)
