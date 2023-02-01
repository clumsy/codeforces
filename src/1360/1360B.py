t = int(input())
for _ in range(t):
    n, s = int(input()), sorted(int(i) for i in input().split())
    res = s[-1] - s[0]
    for i in range(1, n):
        res = min(res, s[i] - s[i - 1])
    print(res)
