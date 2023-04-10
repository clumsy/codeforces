n, k = (int(i) for i in input().split())
a = sorted(int(i) for i in input().split())
res = a[n - k]
print(res)
