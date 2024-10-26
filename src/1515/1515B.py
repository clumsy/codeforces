from math import isqrt


t = int(input())
for _ in range(t):
    n = int(input())
    res = (
        "YES"
        if (n % 2 == 0 and isqrt(n // 2) ** 2 == n // 2)
        or (n % 4 == 0 and isqrt(n // 4) ** 2 == n // 4)
        else "NO"
    )
    print(res)
