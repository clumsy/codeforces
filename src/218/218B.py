n, m = (int(i) for i in input().split())
a = sorted(int(i) for i in input().split())
mi, cur = 0, n
for e in a:
    d = min(e, cur)
    mi += (e + 1 - d + e) * d // 2
    cur -= d
    if not cur:
        break
ma, cur = 0, n
while cur:
    for i in range(m)[::-1]:
        if not cur or a[i] < a[-1]:
            break
        ma += a[i]
        a[i] -= 1
        cur -= 1
res = ma, mi
print(*res)
