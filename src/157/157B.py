from math import pi

n, r = int(input()), sorted((int(i) for i in input().split()), reverse=True)
res = pi * sum((-1) ** i * x**2 for i, x in enumerate(r))
print(res)
