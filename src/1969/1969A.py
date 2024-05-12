t = int(input())
for _ in range(t):
    n, p = int(input()), [int(i) for i in input().split()]
    res = 3
    for i in range(n):
        if p[p[i] - 1] == i + 1:
            res = 2
            break
    print(res)
