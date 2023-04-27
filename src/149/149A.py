k, a = int(input()), (int(i) for i in input().split())
a = sorted(a, reverse=True)
res = 0
while res < len(a) and k > 0:
    k -= a[res]
    res += 1
res = res if k <= 0 else -1
print(res)
