t = int(input())
for _ in range(t):
    n, p = int(input()), (int(i) for i in input().split())
    pos = [-1] * n
    for i, v in enumerate(p):
        pos[v - 1] = i
    res = "YES"
    for i in range(n):
        if abs(pos[i] - i) > 1:
            res = "NO"
    print(res)
