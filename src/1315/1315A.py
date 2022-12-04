t = int(input())
for _ in range(t):
    a, b, x, y = (int(i) for i in input().split())
    res = max(max(x, a - x - 1) * b, a * max(y, b - y - 1))
    print(res)
