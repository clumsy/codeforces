t = int(input())
for _ in range(t):
    n = int(input())
    if n in {1, 2, 4}:
        res = [-1]
    else:
        r = n % 3
        if r == 0:
            res = [n // 3, 0, 0]
        elif r == 1:
            res = [(n - 7) // 3, 0, 1]
        else:  # r == 2
            res = [(n - 5) // 3, 1, 0]
    print(*res)
