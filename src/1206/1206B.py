n = int(input())
a = (int(i) for i in input().split())
res, zeros, negs = 0, 0, 0
for i in a:
    if i >= 1:
        res += i - 1
    elif i == 0:
        zeros += 1
    else:
        res += -(i + 1)
        negs += 1
if negs & 1 != 0 and zeros == 0:
    # either 1 -> -1 or -1 -> 1
    res += 2
res += zeros
print(res)
