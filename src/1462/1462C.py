t = int(input())
for _ in range(t):
    x = int(input())
    res = []
    acc, digit = 0, 9
    while acc < x and digit > 0:
        res.append(min(x - acc, digit))
        acc += res[-1]
        digit -= 1
    res = "".join(str(i) for i in reversed(res)) if acc == x else -1
    print(res)
