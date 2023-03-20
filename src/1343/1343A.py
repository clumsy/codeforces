t = int(input())
for _ in range(t):
    n = int(input())
    # x * (2^k - 1)/(2 - 1) = n => x * (2^k - 1) = n
    p = 4
    while p - 1 <= n:
        d, r = divmod(n, p - 1)
        if r == 0:
            res = d
            break
        p *= 2
    print(res)
