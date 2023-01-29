n = int(input())
m = [[int(i) for i in input().split()] for _ in range(n)]
res = 0
for r in range(n):
    for c in range(n):
        if r == c or r + c == n - 1 or r == (n - 1) / 2 or c == (n - 1) / 2:
            res += m[r][c]
print(res)
