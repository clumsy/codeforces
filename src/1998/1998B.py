t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = a[1:] + [a[0]]
    print(*res)
