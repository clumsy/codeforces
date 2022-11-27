t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    count = [0] * 101
    for i in a:
        count[i] += 1
    res = []
    for i in range(101):
        if count[i] > 0:
            res.append(i)
            count[i] -= 1
    for i in range(101):
        while count[i]:
            res.append(i)
            count[i] -= 1
    print(*res)
