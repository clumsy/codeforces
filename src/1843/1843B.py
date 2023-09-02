t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    s = c = 0
    started = False
    for i in a:
        if i < 0 and not started:
            c += 1
            started = True
        if i > 0:
            started = False
        s += abs(i)
    res = s, c
    print(*res)
