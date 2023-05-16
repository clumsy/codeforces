t = int(input())
for _ in range(t):
    n, q = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    for i in range(1, n):
        a[i] += a[i - 1]
    for _ in range(q):
        le, r, k = (int(i) for i in input().split())
        s = a[-1] - (a[r - 1] - (0 if le == 1 else a[le - 2])) + k * (r - le + 1)
        res = "YES" if s & 1 == 1 else "NO"
        print(res)
