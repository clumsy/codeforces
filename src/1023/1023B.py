n, k = (int(i) for i in input().split())
mi = min(n, (k - 1) // 2)
# k - l <= n
res = max(0, mi - (k - n - 1 if k > n else 0))
print(res)
