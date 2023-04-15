from itertools import islice

na, nb = (int(i) for i in input().split())
k, m = (int(i) for i in input().split())
a = (int(i) for i in input().split())
b = reversed(list(int(i) for i in input().split()))
res = "YES" if next(islice(a, k - 1, None)) < next(islice(b, m - 1, None)) else "NO"
print(res)
