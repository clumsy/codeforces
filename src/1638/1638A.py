t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    for i in range(n):
        if a[i] != i + 1:
            j = a.index(i + 1, i + 1)
            while i < j:
                a[i], a[j] = a[j], a[i]
                i, j = i + 1, j - 1
            break
    print(*a)
