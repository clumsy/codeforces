t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    if a[0] < a[-1]:
        a.reverse()
    res = "YES"
    for i in range(n):
        if a[i] <= 2 * max(i, n - 1 - i):
            res = "NO"
            break
    print(res)
