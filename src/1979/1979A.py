t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = min(max(a[i], a[i + 1]) for i in range(n - 1)) - 1
    print(res)
