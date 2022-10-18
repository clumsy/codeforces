n = int(input())
lc, rc = 0, 0
for _ in range(n):
    d = input().split()
    lc += d[0] == "0"
    rc += d[1] == "0"
res = min(lc, n - lc) + min(rc, n - rc)
print(res)
