n, m = (int(input()) for _ in range(2))
a = reversed(sorted(int(input()) for _ in range(n)))
res = 0
while m > 0:
    m -= next(a)
    res += 1
print(res)
