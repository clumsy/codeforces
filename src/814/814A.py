n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
b = sorted((int(i) for i in input().split()), reverse=True)
res, j = "NO", 0
for i, e in enumerate(a):
    if a[i] == 0:
        a[i] = b[j]
        j += 1
    if i > 0 and a[i] <= a[i - 1]:
        res = "YES"
        break
print(res)
