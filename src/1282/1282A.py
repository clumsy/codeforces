t = int(input())
for _ in range(t):
    a, b, c, r = (int(i) for i in input().split())
    a, b = sorted([a, b])
    res = abs(b - a) - abs(
        min(b, (c + r) if c + r >= a else a) - max(a, (c - r) if c - r <= b else b)
    )
    print(res)
