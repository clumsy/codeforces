t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    res = list(range(n, m, -1)) + list(range(1, m + 1))
    print(*res)
