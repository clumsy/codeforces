t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = [n + 1 - i for i in a]
    print(*res)
