t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    d, r = divmod(n, m)
    res = "YES" if n - (d + (1 if r else 0)) > k else "NO"
    print(res)
