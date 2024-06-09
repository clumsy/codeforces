from math import sqrt


a, b, c = (int(i) for i in input().split())
# x * y = a
# x * z = b
# z * y = c
# y/z = a/b
# y = za/b
# z^2 = cb/a
z = sqrt(c * b / a)
# y = z * a / b
y = sqrt(c * a / b)
x = sqrt(a * b / c)
res = 4 * int(x + y + z)
print(res)
