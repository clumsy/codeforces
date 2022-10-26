t = int(input())
for _ in range(t):
    a, b, c, d, k = (int(i) for i in input().split())
    x = (a + c - 1) // c
    y = (b + d - 1) // d
    res = (-1,) if x + y > k else (x, y)
    print(*res)
