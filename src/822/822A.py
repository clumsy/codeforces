from math import factorial

a, b = (int(i) for i in input().split())
res = factorial(min(a, b))
print(res)
