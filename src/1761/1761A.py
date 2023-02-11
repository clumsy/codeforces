t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    res = "YES" if n == a == b or n - (a + b) > 1 else "NO"
    print(res)
