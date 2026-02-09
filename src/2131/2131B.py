from itertools import islice


t = int(input())
for _ in range(t):
    n = int(input())
    res = list(islice([-1, 3] * ((n + 1) // 2), n))
    if n & 1 == 0:
        res[-1] -= 1
    print(*res)
