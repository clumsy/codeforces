t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = [1] * n if k == n else range(1, n + 1) if k == 1 else [-1]
    print(*res)
