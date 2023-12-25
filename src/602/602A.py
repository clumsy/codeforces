def convert(x, b):
    v = next(x)
    for i in x:
        v = v * b + i
    return v


n, bx = (int(i) for i in input().split())
x = (int(i) for i in input().split())
x = convert(x, bx)
n, by = (int(i) for i in input().split())
y = (int(i) for i in input().split())
y = convert(y, by)
res = "=" if x == y else "<" if x < y else ">"
print(res)
