n, s = int(input()), list(input())
d = [i for i in range(1, n + 1) if n % i == 0]
for i, e in enumerate(d):
    s[:e] = reversed(s[:e])
res = "".join(s)
print(res)
