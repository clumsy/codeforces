n, a = int(input()), list(input())
down, half = a.count("x"), n // 2
res = abs(down - half)
print(res)
for i, c in enumerate(a):
    if down > half and c == "x":
        a[i] = "X"
        res -= 1
    if down < half and c == "X":
        a[i] = "x"
        res -= 1
    if res == 0:
        break
res = "".join(a)
print(res)
