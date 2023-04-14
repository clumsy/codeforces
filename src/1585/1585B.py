t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, cur = 0, a[-1]
    for i in a[::-1]:
        if i > cur:
            res += 1
            cur = i
    print(res)
