t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, o = 0, []
    for i in a:
        if i & 1 == 0:
            res += i
        else:
            o.append(i)
    if o:
        o.sort()
        res += sum(o[len(o) // 2 :])
    else:
        res = 0
    print(res)
