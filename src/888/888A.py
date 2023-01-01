n, a = int(input()), [int(i) for i in input().split()]
res = sum(
    a[i - 1] < a[i] > a[i + 1] or a[i - 1] > a[i] < a[i + 1] for i in range(1, n - 1)
)
print(res)
