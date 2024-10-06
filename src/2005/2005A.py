t = int(input())
for _ in range(t):
    n = int(input())
    if n == 4:
        res = "aioe"
    elif n == 3:
        res = "aio"
    elif n == 2:
        res = "ai"
    else:
        u, r = divmod(n, 5)
        i = u + (1 if r > 0 else 0)
        a = u + (1 if r > 1 else 0)
        e = u + (1 if r > 2 else 0)
        o = u + (1 if r > 3 else 0)
        res = "a" * a + "o" * o + "i" * i + "u" * u + "e" * e
    print(res)
