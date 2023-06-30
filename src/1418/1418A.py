t = int(input())
for _ in range(t):
    x, y, k = (int(i) for i in input().split())
    # 1 + r * x - r >= k * y + k
    res = k + (k * y + k + x - 3) // (x - 1)
    print(res)
