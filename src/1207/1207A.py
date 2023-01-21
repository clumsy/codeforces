t = int(input())
for _ in range(t):
    b, p, f = (int(i) for i in input().split())
    h, c = (int(i) for i in input().split())
    p, f, h, c = (p, f, h, c) if h > c else (f, p, c, h)
    res = h * min(b // 2, p) + c * max(0, min(b // 2 - p, f))
    print(res)
