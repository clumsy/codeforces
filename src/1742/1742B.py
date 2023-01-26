t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = "YES"
    for i in range(1, n):
        if a[i] == a[i - 1]:
            res = "NO"
            break
    print(res)
