t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = (0, 0) if sum(a) % 3 != 0 else (1, 2)
    print(*res)
