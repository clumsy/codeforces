from math import gcd

n, m, z = (int(i) for i in input().split())
lcm = n * m // gcd(n, m)
res = z // lcm
print(res)
