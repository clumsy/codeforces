t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res, k = 0, 1
    for i in range(n):
        res += max(a[i] - k, 0)
        if a[i] >= k:
            k += 1
    print(res)
