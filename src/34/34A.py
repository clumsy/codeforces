n, a = int(input()), [int(i) for i in input().split()]
l, r = 0, 1
for i in range(n):
    if abs(a[i - 1] - a[i]) < abs(a[l] - a[r]):
        l, r = i - 1, i
res = l % n + 1, r % n + 1
print(*res)
