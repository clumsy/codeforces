t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = next(a)
    for i in a:
        res = i * ((res + i) // i)
    print(res)
