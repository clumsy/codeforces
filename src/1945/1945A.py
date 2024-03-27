t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    bd, br = divmod(b, 3)
    if 0 < br < 3 - c:
        res = -1
    else:
        c -= 3 - br
        res = a + bd + 1 + (c + 2) // 3
    print(res)
