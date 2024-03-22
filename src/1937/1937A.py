t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    while res * 2 <= n:
        res *= 2
    print(res)
