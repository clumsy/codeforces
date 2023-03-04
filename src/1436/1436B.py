t = int(input())
for _ in range(t):
    n = int(input())
    res = [[int(c == r or c == (r + 1) % n) for c in range(n)] for r in range(n)]
    for i in range(n):
        print(*res[i])
