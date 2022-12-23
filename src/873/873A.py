n, k, x = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
for i in range(n - k, n):
    a[i] = min(a[i], x)
res = sum(a)
print(res)
