from math import isqrt


t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = (int(i) for i in input().split())
    if b1 > l1:
        l1, l2, l3, b1, b2, b3 = b1, b2, b3, l1, l2, l3
    a = l1 * b1 + l2 * b2 + l3 * b3
    s = isqrt(a)
    res = (
        "YES"
        if (
            s**2 == a
            and (
                (l1 == l2 == l3 == s and b1 + b2 + b3 == s)
                or (l1 == s and l2 + l3 == s and b1 + b2 == s and b2 == b3)
            )
        )
        else "NO"
    )
    print(res)
