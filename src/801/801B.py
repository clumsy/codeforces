x, y = input(), input()
res = y if all(y[i] <= x[i] for i in range(len(x))) else -1
print(res)
