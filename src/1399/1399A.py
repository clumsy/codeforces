t = int(input())
for _ in range(t):
    n = int(input())
    a = sorted(int(i) for i in input().split())
    res = "NO" if any(a[i + 1] - a[i] > 1 for i in range(n - 1)) else "YES"
    print(res)
