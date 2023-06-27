x, y = (int(i) for i in input().split())
# Z - x = Z - y
# area(ABC) = area(xy) + area(triag1) + area(triag2)
# 0.5Z^2 = xy + 0.5y(Z - x) + 0.5x(Z - y)
# 0.5Z^2 = xy + 0.5Zy - xy + 0.5Zx
# Z^2 = (x + y)Z
# Z = x + y
res = abs(x) + abs(y)
res = sorted([((x // abs(x)) * res, 0), (0, (y // abs(y)) * res)])
res = *res[0], *res[1]
print(*res)
