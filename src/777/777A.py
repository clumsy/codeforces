n, x = (int(input()) for _ in range(2))
m = [
    [0, 1, 2],
    [1, 0, 2],
    [1, 2, 0],
    [2, 1, 0],
    [2, 0, 1],
    [0, 2, 1],
]
res = m[n % 6][x]
print(res)
