t = int(input())
for _ in range(t):
    n, x, a, b = (int(i) for i in input().split())
    res = min(n - 1, abs(a - b) + x)
    print(res)
