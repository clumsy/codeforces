t = int(input())
for _ in range(t):
    n, p = int(input()), [int(i) for i in input().split()]
    if n == 1:
        res = [-1]
    else:
        res = [i for i in range(1, n + 1)]
        for i in range(n):
            if res[i] == p[i]:
                j = i + 1 if i < n - 1 else i - 1
                res[j], res[i] = res[i], res[j]
    print(*res)
