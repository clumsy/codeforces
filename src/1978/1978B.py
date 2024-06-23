t = int(input())


def f(n, a, b, k):
    return b * k - (k - 1) * k // 2 + (n - k) * a
    # bk + b - k^2/2 - k/2 + na - ak - a
    # derivative: b - k - 1/2 - a = 0
    # k = b - a - 1/2, maximums at b - a - 1 and b - a


for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    res = max(
        f(n, a, b, k) for k in (0, min(n, max(0, b - a - 1)), min(n, max(0, b - a)))
    )
    print(res)
