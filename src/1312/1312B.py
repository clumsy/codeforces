t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = sorted(a, reverse=True)
    print(*res)
