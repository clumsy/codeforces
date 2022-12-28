a, b = sorted(int(input()) for _ in range(2))
n = (b - a) // 2
res = (n + 1) * n
if b - a > 2 * n:
    res += n + 1
print(res)
