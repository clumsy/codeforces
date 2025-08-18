t = int(input())
for _ in range(t):
    k, a, b, x, y = (int(i) for i in input().split())
    r1 = max(0, (k - a) // x + 1)
    r1 += max(0, (k - x * r1 - b) // y + 1)
    r2 = max(0, (k - b) // y + 1)
    r2 += max(0, (k - y * r2 - a) // x + 1)
    res = max(r1, r2)
    print(res)
