from itertools import accumulate

n, a = int(input()), [int(i) for i in input().split()]
d, r = divmod(n, sum(a))
n -= (d - (r == 0)) * sum(a)
res = next(i + 1 for i, e in enumerate(accumulate(a)) if e >= n)
print(res)
