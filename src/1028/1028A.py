n, m = (int(i) for i in input().split())
t = [input() for _ in range(n)]
for r in range(n):
    for c in range(m):
        if t[r][c] == "B":
            break
    else:
        continue
    break
d = (t[r].rfind("B") - c) // 2
res = r + d + 1, c + d + 1
print(*res)
