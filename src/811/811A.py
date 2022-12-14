from math import floor, sqrt

a, b = (int(i) for i in input().split())
# a = (2*1 + (vl - 1)*2)*vl/2 => a = vl + vl^2 - vl => vl = sqrt(a)
# b = (2*2 + (va - 1)*2)*va/2 => b = 2va + va^2 - va => va^2 + va - b = 0 => va = (-1 + sqrt(1 + 4b))/2
vladik = floor(sqrt(a))
valera = floor((sqrt(4 * b + 1) - 1) / 2)
res = "Vladik" if valera >= vladik else "Valera"
print(res)
