t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = [1, 2, n] if a[0] + a[1] <= a[-1] else [-1]
    print(*res)
