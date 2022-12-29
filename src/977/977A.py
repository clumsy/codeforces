res, k = (int(i) for i in input().split())
while k > 0:
    d, m = divmod(res, 10)
    if m < k:
        res, k = d, k - m - 1
    else:
        res -= k
        break
print(res)
