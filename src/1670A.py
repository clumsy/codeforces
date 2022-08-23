t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    minuses = 0
    for i in range(n):
        if a[i] < 0:
            minuses += 1
            a[i] *= -1
    for i in range(minuses):
        a[i] *= -1
    res = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            res = False
            break
    print("YES" if res else "NO")
