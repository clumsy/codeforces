t = int(input())
for _ in range(t):
    n = int(input())
    print(n)
    a = [i + 1 for i in range(n)]
    for i in range(n):
        print(*a)
        a[i], a[n - 1] = a[n - 1], a[i]
