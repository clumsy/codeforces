n, m = (int(i) for i in input().split())
s, t = (input() for _ in range(2))
res = list(range(1, n + 1))
for i in range(m - n + 1):
    cur = []
    for j in range(n):
        if t[i + j] != s[j]:
            cur.append(j + 1)
    if len(cur) < len(res):
        res = cur
print(len(res))
print(*res)
