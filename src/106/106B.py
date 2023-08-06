n = int(input())
s, r, h, c = [0] * n, [0] * n, [0] * n, [0] * n
for i in range(n):
    s[i], r[i], h[i], c[i] = (int(i) for i in input().split())
order = sorted(range(n), key=c.__getitem__)
res = -1
for i in order:
    for j in range(n):
        if s[j] > s[i] and r[j] > r[i] and h[j] > h[i]:
            break
    else:
        res = i + 1
        break
print(res)
