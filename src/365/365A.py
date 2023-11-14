n, k = (int(i) for i in input().split())
res, digits = 0, {str(d) for d in range(0, k + 1)}
for _ in range(n):
    x = input()
    res += len(digits - set(x)) == 0
print(res)
