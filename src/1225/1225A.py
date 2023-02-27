a, b = (int(i) for i in input().split())
if a == b:
    res = a * 10, b * 10 + 1
elif a == 9 and b == 1:
    res = 9, 10
elif b - a == 1:
    res = a, b
else:
    res = [-1]
print(*res)
