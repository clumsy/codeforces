t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    if a[0] == -1:
        a[0] = a[n - 1]
    if a[-1] == -1:
        a[-1] = a[0]
    for i in range(n):
        a[i] = max(a[i], 0)
    res = abs(a[-1] - a[0])
    print(res)
    print(*a)
