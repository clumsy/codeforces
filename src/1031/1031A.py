w, h, k = (int(i) for i in input().split())
res = 0
while w > 0 and h > 2 and k > 0:
    res += 2 * w + 2 * (h - 2)
    w -= 4
    h -= 4
    k -= 1
print(res)
