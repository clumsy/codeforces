t = int(input())


def f(x, a):
    return x // a + x % a


for _ in range(t):
    l, r, a = (int(i) for i in input().split())
    x = r if r % a == a - 1 else max(r - (r % a) - 1, l)
    res = max(f(x, a), f(r, a))
    print(res)
