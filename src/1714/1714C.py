t = int(input())

for _ in range(t):
    s = int(input())
    res, power, last = 0, 1, 10
    while s > 0:
        last = min(s, last - 1)
        s -= last
        res = last * power + res
        power *= 10
    print(res)
