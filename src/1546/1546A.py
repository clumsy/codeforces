t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    if sum(a) != sum(b):
        print("-1")
        continue
    for i in range(n):
        a[i] -= b[i]
    p = sum(a[i] for i in range(n) if a[i] > 0)
    print(p)
    i, j = 0, 0
    for _ in range(p):
        while i < n and a[i] <= 0:
            i += 1
        while j < n and a[j] >= 0:
            j += 1
        a[i] -= 1
        a[j] += 1
        print(i + 1, j + 1)
