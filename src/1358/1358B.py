t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = 1
    for i in range(n - 1, -1, -1):
        if a[i] <= i + 1:
            res = i + 2
            break
    print(res)
