n, m, k = (int(i) for i in input().split())
a = sorted((int(i) for i in input().split()), reverse=True)
res = -1
for i in range(n):
    if k >= m:
        res = i
        break
    k += a[i] - 1
res = res if res >= 0 else n if k >= m else -1
print(res)
