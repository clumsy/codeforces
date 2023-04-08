from math import sqrt

n, a = int(input()), (int(i) for i in input().split())
a = sorted(a, reverse=True)
for i in a:
    if i < 0 or int(sqrt(i)) ** 2 != i:
        res = i
        break
print(res)
