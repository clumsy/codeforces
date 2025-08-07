t = int(input())
for _ in range(t):
    n, c = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, rem = 0, []
    for i in a:
        if i > c:
            res += 1
        else:
            rem.append(i)
    rem.sort()
    ftr = 1
    while rem:
        cur = rem.pop()
        if cur * ftr > c:
            res += 1
        else:
            ftr *= 2
    print(res)
