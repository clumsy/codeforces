t = int(input())
for _ in range(t):
    n = int(input())
    if n - 3 & 1 == 1:
        res = 2, n - 3, 1
    else:
        x, i = (n - 1) // 2, 1
        while x - i & 1 == x + i & 1 == 0:
            i += 1
        res = x - i, x + i, 1
    print(*res)
