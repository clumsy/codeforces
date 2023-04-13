n, k = (int(i) for i in input().split())
a = sorted(int(i) for i in input().split())
res = [-1] if k > n else [a[n - k], 0]
print(*res)
