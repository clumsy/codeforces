t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = min(n, 2), min(m, 2)
    print(*res)
