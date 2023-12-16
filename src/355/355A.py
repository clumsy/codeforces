k, d = (int(i) for i in input().split())
if d == 0 and k > 1:
    res = "No solution"
elif k == 1:
    res = str(d)
else:
    res = ["0"] * k
    res[0], res[-1] = "1", str(d - 1)
    res = "".join(res)
print(res)
