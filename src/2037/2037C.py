t = int(input())
for _ in range(t):
    n = int(input())
    if n < 5:
        res = [-1]
    else:
        evn, odd = [i for i in range(2, n + 1, 2)], [i for i in range(1, n + 1, 2)]
        evn[1], evn[-1] = evn[-1], evn[1]
        odd[0], odd[2] = odd[2], odd[0]
        res = evn + odd
    print(*res)
