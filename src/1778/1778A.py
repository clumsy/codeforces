t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    m = min(a[i] + a[i + 1] for i in range(n - 1))
    res = sum(a) - 2 * m
    print(res)
