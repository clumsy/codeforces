n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res = 0
for i in range(1, n):
    diff = k - (a[i - 1] + a[i])
    if diff > 0:
        res += diff
        a[i] += diff
print(res)
print(*a)
