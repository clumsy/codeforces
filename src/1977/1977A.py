t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = "YES" if n >= m and (n - m) & 1 == 0 else "NO"
    print(res)
