n = int(input())
res = ["o"] * n
a, b = 1, 1
while a <= n:
    res[a - 1] = "O"
    a, b = b, a + b
res = "".join(res)
print(res)
