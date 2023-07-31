n = int(input())
res = 0
for i in range(n):
    res += 1 + (n - 1 - i) * (i + 1)
print(res)
