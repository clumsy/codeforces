x = int(input())
res = 0
while x:
    x -= x & -x
    res += 1
print(res)
