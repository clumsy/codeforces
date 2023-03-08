b, k = (int(i[-1]) for i in input().split())
a = [int(i[-1]) for i in input().split()]
res, p = 0, 1
for i in reversed(a):
    res = (res + i * p) % 10
    p = (p * b) % 10
res = "even" if res & 1 == 0 else "odd"
print(res)
