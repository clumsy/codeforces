n, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
res, arya = 0, 0
for i in a:
    arya += i
    give = min(8, arya)
    k -= give
    arya -= give
    res += 1
    if k <= 0:
        break
res = res if k <= 0 else -1
print(res)
