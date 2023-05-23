t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        res = [1]
    elif n & 1 == 1:
        res = [-1]
    else:
        # 2 1 4 3
        res = [i for a, b in zip(range(2, n + 1, 2), range(1, n, 2)) for i in (a, b)]
    print(*res)
