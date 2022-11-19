T = int(input())
for _ in range(T):
    n, a = int(input()), [int(i) for i in input().split()]
    res = [0] * n
    for i in range(0, n, 2):
        res[i], res[i + 1] = -a[i + 1], a[i]
    print(*res)
