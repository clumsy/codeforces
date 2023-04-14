from functools import reduce
from operator import ior

n = int(input())
a = (int(i) for i in input().split())
b = (int(i) for i in input().split())
a = reduce(ior, a)
b = reduce(ior, b)
res = a + b
print(res)
