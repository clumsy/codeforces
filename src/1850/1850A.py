t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "YES" if max(a + b, b + c, a + c) >= 10 else "NO"
    print(res)
