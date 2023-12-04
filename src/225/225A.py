n, x = (int(input()) for _ in range(2))
res = "YES"
dice = set(range(1, 7))
for _ in range(n):
    a, b = (int(i) for i in input().split())
    s = {7 - x, a, 7 - a, b, 7 - b}
    if len(s) < 5:
        res = "NO"
        break
    x = (dice - s).pop()
print(res)
