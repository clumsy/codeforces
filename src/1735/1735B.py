t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    mi = min(a)
    res = sum((i + 2 * mi - 2) // (2 * mi - 1) - 1 for i in a)
    print(res)
