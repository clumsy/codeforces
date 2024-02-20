from functools import reduce
from operator import mul


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    prd = reduce(mul, a)
    res = 0 if prd <= 0 else [1, 0]
    if res == 0:
        print(res)
    else:
        print(1)
        print(*res)
