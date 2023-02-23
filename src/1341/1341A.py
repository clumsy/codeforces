t = int(input())
for _ in range(t):
    n, a, b, c, d = (int(i) for i in input().split())
    res = "YES" if n * (a - b) <= c + d and n * (a + b) >= c - d else "NO"
    print(res)
