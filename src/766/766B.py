n, a = int(input()), sorted(int(i) for i in input().split())
res = "NO"
for i in range(n - 2):
    if a[i] + a[i + 1] > a[i + 2]:
        res = "YES"
        break
print(res)
