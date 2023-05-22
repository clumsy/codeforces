t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    b = sorted(int(i) for i in input().split())
    order = sorted(range(n), key=a.__getitem__)
    res = [None] * n
    for i in range(n):
        res[order[i]] = b[i]
    print(*res)
