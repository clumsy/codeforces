n, m = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
res = 0
for i in range(1, m):
    if a[i] < a[i - 1]:
        res += n
    if i == m - 1:
        res += a[i] - 1
print(res)
