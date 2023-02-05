from functools import reduce
from operator import mul

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    # make it 1 1 ... 1 prod(a)
    res = 2022 * (reduce(mul, a) + n - 1)
    print(res)
