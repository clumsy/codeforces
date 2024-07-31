t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "NO"
    if n <= 2 and abs(next(a) - next(a)) > 1:
        res = "YES"
    print(res)
