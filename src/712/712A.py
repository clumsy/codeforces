n, a = int(input()), [int(i) for i in input().split()]
res = [0] * n
s, bs = 1, 0
# an = bn => bn = an
# an-1 = bn-1 - bn => bn-1 = an-1 + bn
# bk = ak + s * bs
for i in reversed(range(n)):
    res[i] = a[i] + s * bs
    s *= -1
    bs += s * res[i]
print(*res)
