t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = 0
    for i in a:
        res = max(0, res + i)
    print(res)
