from itertools import takewhile

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = sum(1 for _ in takewhile(lambda i: 0 < i >= a[k-1], a))
print(res)
