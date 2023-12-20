n = int(input())
a = sorted(int(i) for i in input().split())
mi, c = a[1] - a[0], 1
for i in range(2, n):
    d = a[i] - a[i - 1]
    if d < mi:
        mi, c = d, 0
    if d == mi:
        c += 1
res = mi, c
print(*res)
