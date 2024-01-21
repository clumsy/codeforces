n = int(input())
res = [-1]
for i in range(4):
    a, b, c, d = (int(i) for i in input().split())
    if n >= min(a, b) + min(c, d):
        res = i + 1, min(a, b), n - min(a, b)
print(*res)
