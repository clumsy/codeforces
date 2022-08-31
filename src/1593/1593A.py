t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = (
        max(max(b, c) + 1 - a, 0),
        max(max(a, c) + 1 - b, 0),
        max(max(b, a) + 1 - c, 0),
    )
    print(*res)
