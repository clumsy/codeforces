t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    a.sort()
    res = sum(a[i] - a[i - 1] for i in range(1, n))
    print(res)
