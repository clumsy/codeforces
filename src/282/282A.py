n, x = int(input()), 0
for _ in range(n):
    x += 1 if "++" in input() else -1
print(x)
