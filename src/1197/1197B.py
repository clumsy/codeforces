n, a = int(input()), [int(i) for i in input().split()]
lo = hi = a.index(n)
k = n
while (lo >= 0 and a[lo] == k) or (hi < n and a[hi] == k):
    if lo >= 0 and a[lo] == k:
        lo -= 1
    if hi < n and a[hi] == k:
        hi += 1
    k -= 1
res = "YES" if k == 0 else "NO"
print(res)
