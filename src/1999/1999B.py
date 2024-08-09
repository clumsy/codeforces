t = int(input())
for _ in range(t):
    a1, a2, b1, b2 = (int(i) for i in input().split())
    a1, a2 = sorted([a1, a2])
    b1, b2 = sorted([b1, b2])
    res = (
        4
        if a1 > b2 or (a1 == b2 and a2 > b2) or (a1 == a2 == b2 and a1 > b1)
        else 2
        if (a2 > b2 and a1 >= b1) or (a2 == b2 and a1 > b1)
        else 0
    )
    print(res)
