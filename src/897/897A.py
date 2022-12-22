n, m = (int(i) for i in input().split())
s = list(input())
for _ in range(m):
    l, r, c1, c2 = (int(v) if i < 2 else v for i, v in enumerate(input().split()))
    for i in range(l - 1, r):
        s[i] = c2 if s[i] == c1 else s[i]
res = "".join(s)
print(res)
