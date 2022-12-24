n = int(input())
res = (n - 1) // 2, (n + 2) // 2
if all(i & 1 == 0 for i in res):
    res = res[0] - 1, res[1] + 1
print(*res)
