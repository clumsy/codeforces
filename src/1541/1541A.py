t = int(input())
for _ in range(t):
    n = int(input())
    res, s = [], 2
    if n & 1 == 1:
        res += [3, 1, 2]
        s = 5
    res += [i for pair in zip(range(s, n + 1, 2), range(s - 1, n + 1, 2)) for i in pair]
    print(*res)
