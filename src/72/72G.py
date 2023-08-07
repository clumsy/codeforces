n = int(input())
a = b = 1
while n > 1:
    n -= 1
    a, b = b, a + b
res = b
print(res)
