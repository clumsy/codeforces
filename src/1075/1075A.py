n, [x, y] = int(input()), (int(i) for i in input().split())
res = "White" if x - 1 + y - 1 <= n - x + n - y else "Black"
print(res)
