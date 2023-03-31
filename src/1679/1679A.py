t = int(input())
for _ in range(t):
    n = int(input())
    # 4x + 6y = n
    # 2x + 3y = n/2 and n is even
    if n & 1 == 1 or n < 4:
        res = [-1]
    else:
        half = n // 2
        ma = half // 2 if half & 1 == 0 else 1 + (half - 3) // 2
        mi = (
            half // 3
            if half % 3 == 0
            else 1 + (half - 2) // 3
            if half % 3 == 2
            else 2 + (half - 2 * 2) // 3
        )
        res = mi, ma
    print(*res)
