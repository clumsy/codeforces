t = int(input())
for _ in range(t):
    l1, r1, l2, r2 = (int(i) for i in input().split())
    max_l, min_r = max(l1, l2), min(r1, r2)
    if max_l <= min_r:
        print(max_l)
    else:
        print(l1 + l2)
