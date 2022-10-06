t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    # x = a < y = z = c
    res = a, c, c
    print(*res)
