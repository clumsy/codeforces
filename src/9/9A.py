y, w = (int(i) for i in input().split())
a, b = 7 - max(y, w), 6
for i in range(2, 7):
    while a % i == 0 and b % i == 0:
        a, b = a // i, b // i
res = f"{a}/{b}"
print(res)
