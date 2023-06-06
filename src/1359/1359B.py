t = int(input())


def price(c, x, y):
    t, o = divmod(c, 2)
    return o * x + min(2 * t * x, t * y)


for _ in range(t):
    n, m, x, y = (int(i) for i in input().split())
    res = 0
    for _ in range(n):
        res += sum(price(len(c), x, y) for c in input().split("*"))
    print(res)
