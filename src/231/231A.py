n = int(input())
res = 0
for _ in range(n):
    res += 1 if input().count("1") > 1 else 0
print(res)
