t = int(input())
for _ in range(t):
    n, b = int(input()), (int(i) for i in input().split())
    res = [next(b)]
    for i in b:
        if i < res[-1]:
            res.append(i)
        res.append(i)
    print(len(res))
    print(*res)
