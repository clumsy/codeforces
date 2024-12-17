a, b = (int(i) for i in input().split())
res = 0
while min(a, b) > 0 and max(a, b) > 1:
    if a > b:
        a, b = b, a
    a, b = a + 1, b - 2
    res += 1
print(res)
