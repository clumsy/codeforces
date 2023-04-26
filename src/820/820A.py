c, v0, v1, a, l_ = (int(i) for i in input().split())
res, v = 0, v0
while c > 0:
    c -= v - l_ if res > 0 else v
    v = min(v1, v + a)
    res += 1
print(res)
