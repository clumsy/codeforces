n = int(input())
res = cur = 0
p = None
for _ in range(n):
    s = input()
    cur = cur + 1 if s == p else 1
    p = s
    res = max(res, cur)
print(res)
