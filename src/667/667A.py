from math import pi

d, h, v, e = (int(i) for i in input().split())
v = 4 * v / (pi * d**2)
if e >= v:
    res = "NO"
else:
    print("YES")
    res = h / (v - e)
print(res)
