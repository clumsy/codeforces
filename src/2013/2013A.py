t = int(input())
for _ in range(t):
    n = int(input())
    x, y = (int(i) for i in input().split())
    m = min(x, y)
    res = (n + m - 1) // m
    print(res)
