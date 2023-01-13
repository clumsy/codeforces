t = int(input())
for _ in range(t):
    a, b, c, n = (int(i) for i in input().split())
    d, r = divmod(a + b + c + n, 3)
    res = "YES" if r == 0 and all(i <= d for i in (a, b, c)) else "NO"
    print(res)
