t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    i = 0
    while k > 0 and i < n - 1:
        a[i], a[-1], k, i = max(0, a[i] - k), a[-1] + min(a[i], k), k - a[i], i + 1
    print(*a)
