n = int(input())
a = (int(input()) for _ in range(n))
res = [0] * n
for i, e in enumerate(a):
    res[i] = max(res[i - 1] + 1 if i > 0 else 0, e - i - 1)
print(*res, sep="\n")
