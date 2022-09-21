n, m = (int(i) for i in input().split())
s = (1 + n) * n // 2
m = m % s if m >= s else m
for i in range(n):
    if m >= i:
        m -= i
    else:
        break
print(m)
