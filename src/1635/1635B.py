t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    c = 0
    for i in range(1, n - 1):
        if a[i - 1] < a[i] > a[i + 1]:
            if i + 2 < n and a[i] > a[i + 1] < a[i + 2]:
                a[i + 1] = max(a[i], a[i + 2])
            else:
                a[i + 1] = a[i]
            c += 1
    print(c), print(*a)
