t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = "YES" if min(n, m) > 1 and not (n == m == 2) else "NO"
    print(res)
