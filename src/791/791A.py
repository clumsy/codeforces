from math import log, floor

a, b = (int(i) for i in input().split())
# 3^x*a > 2^x*b => (3/2)^x > b/a
# x > log3/2(b/a)
res = floor(log(b / a, 3 / 2) + 1)
print(res)
