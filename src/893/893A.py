n = int(input())
res = "YES"
spec = 3
for _ in range(n):
    won = int(input())
    if won == spec:
        res = "NO"
    spec = 6 - won - spec
print(res)
