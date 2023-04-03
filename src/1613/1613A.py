t = int(input())
for _ in range(t):
    x1, p1 = (int(i) for i in input().split())
    x2, p2 = (int(i) for i in input().split())
    # make x1 smallest
    lt, gt = "<", ">"
    if x2 < x1:
        x1, x2 = x2, x1
        p1, p2 = p2, p1
        lt, gt = gt, lt
    while x1 < x2 and p1 > 0:
        x1 *= 10
        p1 -= 1
    res = "=" if x1 == x2 and p1 == p2 else gt if x1 >= x2 and p1 >= p2 else lt
    print(res)
