t = int(input())
for _ in range(t):
    n, s = int(input()), (int(i) for i in input().split())
    res, val, cnt = [0] * n, None, 0
    for i, e in enumerate(s):
        if e == val:
            cnt += 1
        elif cnt == 1:
            res = [-1]
            break
        if i > 0:
            res[i - 1] = i + 1 if e == val else i - cnt + 1
        if e != val:
            val, cnt = e, 1
    else:
        if cnt < 2:
            res = [-1]
        else:
            res[-1] = n - cnt + 1
    print(*res)
