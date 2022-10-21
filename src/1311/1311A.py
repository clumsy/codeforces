t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    diff = a - b
    res = (
        0
        if diff == 0
        else 1
        if (diff > 0 and diff % 2 == 0) or (diff < 0 and diff % 2 == 1)
        else 2
    )
    print(res)
