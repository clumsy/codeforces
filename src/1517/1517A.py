t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2050 != 0:
        res = -1
    else:
        n, res = n // 2050, 0
        while n:
            res += n % 10
            n //= 10
    print(res)
