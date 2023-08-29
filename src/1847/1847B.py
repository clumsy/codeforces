t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, cur = 0, None
    for i in a:
        cur = cur & i if cur is not None else i
        if cur == 0:
            res += 1
            cur = None
    res = max(res, 1)
    print(res)
