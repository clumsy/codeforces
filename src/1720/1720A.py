t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    x, y = a * d, b * c
    if x == y:
        res = 0  # already equal
    elif (x != 0 and y % x == 0) or (y != 0 and x % y == 0):
        res = 1  # can use one multiplication to make equal
    else:
        res = 2  # multiple both numerators by 0
    print(res)
