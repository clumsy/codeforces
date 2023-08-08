n = int(input())
res, cml = "NO", {}
for i in range(n):
    x, d = (int(i) for i in input().split())
    if x + d in cml and x + d + cml[x + d] == x:
        res = "YES"
    cml[x] = d
print(res)
