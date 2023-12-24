from math import lcm

n, k = (int(i) for i in input().split())
res = lcm(n, 10**k)
print(res)
