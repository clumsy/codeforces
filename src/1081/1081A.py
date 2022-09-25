# we can always pick x=n-1 with no way to minimize the remaining 1, except when v<3
v = int(input())
res = v if v < 3 else 1
print(res)
