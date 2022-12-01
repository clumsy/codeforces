n = int(input())
res, prev = 0, ""
for _ in range(n):
    cur = input()
    res += 1 if cur != prev else 0
    prev = cur
print(res)
