n, m = (int(i) for i in input().split())
c = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
res = 0
for ci in c:
    if res >= m:
        break
    res += ci <= a[res]
print(res)
