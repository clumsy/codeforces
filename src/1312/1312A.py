t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = "YES" if (n // m) * m == n else "NO"
    print(res)
