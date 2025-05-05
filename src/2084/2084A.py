t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1 == 0:
        res = [-1]
    else:
        res = [n] + list(range(1, n))
    print(*res)
