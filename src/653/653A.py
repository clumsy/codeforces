n, t = int(input()), set(int(i) for i in input().split())
res = "NO"
for i in t:
    if i - 1 in t and i + 1 in t:
        res = "YES"
        break
print(res)
