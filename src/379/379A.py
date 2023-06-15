a, b = (int(i) for i in input().split())
res = w = 0
while a:
    res += a
    w += a
    a, w = divmod(w, b)
print(res)
