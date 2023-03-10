n, v = (int(i) for i in input().split())
# if tank is enough for all cities - it's trivial
res = n - 1 if n < v else v - 1
# if not we will spend 1 liter and fill it at next city
for i in range(1, n - v + 1):
    res += i
print(res)
