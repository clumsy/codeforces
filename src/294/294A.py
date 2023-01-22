n, a = int(input()), [int(i) for i in input().split()]
m = int(input())
for _ in range(m):
    x, y = (int(i) for i in input().split())
    if x < n:
        a[x] += a[x - 1] - y
    if x > 1:
        a[x - 2] += y - 1
    a[x - 1] = 0
res = a
print(*res, sep="\n")
