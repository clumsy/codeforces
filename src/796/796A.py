n, m, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res, m = 0, m - 1
for i in range(1, n):
    if (m + i < n and 0 < a[m + i] <= k) or (m - i >= 0 and 0 < a[m - i] <= k):
        res = 10 * i
        break
print(res)
