t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, odd, even = [], [], []
    for i, e in enumerate(a):
        if e & 1 == 1:
            if len(odd) < 3:
                odd.append(i + 1)
        else:
            if len(even) < 2:
                even.append(i + 1)
        if len(odd) > 2:
            res = odd
            break
        if len(even) > 1 and len(odd) > 0:
            res = odd[:1] + even[:2]
            break
    print("YES" if res else "NO")
    if res:
        print(*res)
