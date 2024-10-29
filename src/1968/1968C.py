t = int(input())
for _ in range(t):
    n, x = int(input()), [int(i) for i in input().split()]
    res = [max(x) + 1]
    for i in x:
        res.append(res[-1] + i)
    print(*res)
