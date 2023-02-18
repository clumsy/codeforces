t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    twos = a.count(2)
    res = -1
    if twos & 1 == 0:
        res, cnt = 1, 0
        for i, e in enumerate(a):
            if e == 2:
                cnt += 1
                if 2 * cnt == twos:
                    res = i + 1
                    break
    print(res)
