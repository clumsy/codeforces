n = int(input())
res = "NO"
for _ in range(n):
    _, b, a = (x if i == 0 else int(x) for i, x in enumerate(input().split()))
    if a > b >= 2400:
        res = "YES"
print(res)
