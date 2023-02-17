t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = sum(a[i] & 1 == a[i + 1] & 1 for i in range(n - 1))
    print(res)
