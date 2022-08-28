from itertools import takewhile

n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res = sum(1 for _ in takewhile(lambda i: 0 < i >= a[k - 1], a))
print(res)
