n, s = (int(i) for i in input().split())
f = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
res = (
    "YES"
    if s == 1
    or f[s - 1] == f[0] == 1
    or (f[0] == b[s - 1] == 1 and any(f[i] == b[i] == 1 for i in range(s - 1, n)))
    else "NO"
)
print(res)
