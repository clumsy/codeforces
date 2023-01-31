t = int(input())
for _ in range(t):
    w, d, h = (int(i) for i in input().split())
    a, b, f, g = (int(i) for i in input().split())
    res = min(
        abs(a - f) + (b + g) + h,
        abs(a - f) + (d - b + d - g) + h,
        abs(b - g) + (a + f) + h,
        abs(b - g) + (w - a + w - f) + h,
    )
    print(res)
