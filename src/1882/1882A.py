t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = 0
    for i in a:
        res += 1
        if res == i:
            res += 1
    print(res)
