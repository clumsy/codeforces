t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = (
        sorted(a)
        if sum(i & 1 == 0 for i in a) > 0 and sum(i & 1 == 1 for i in a) > 0
        else a
    )
    print(*res)
