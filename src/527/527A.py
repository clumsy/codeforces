a, b = (int(i) for i in input().split())
res = 0
while b and a != b:
    k, a = divmod(a, b)
    a, b = b, a
    res += k
print(res)
