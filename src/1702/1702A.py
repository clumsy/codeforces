import math

t = int(input())
for _ in range(t):
    m = int(input())
    num_digits = math.floor(math.log10(m) + 1)
    res = m - int(math.pow(10, num_digits - 1))
    print(res)
