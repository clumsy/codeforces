n = int(input())
w, h = [0] * n, [0] * n
ws = 0
hm1 = hm2 = -1
for i in range(n):
    w[i], h[i] = (int(j) for j in input().split())
    ws += w[i]
    if h[i] >= hm1:
        hm1, hm2 = h[i], hm1
    elif h[i] > hm2:
        hm2 = h[i]
res = ((ws - w[i]) * (hm2 if h[i] == hm1 else hm1) for i in range(n))
print(*res)
