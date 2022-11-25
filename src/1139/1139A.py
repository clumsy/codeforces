n, s = int(input()), input()
res, even = 0, {str(i) for i in range(0, 10, 2)}
for i, d in enumerate(s):
    if d in even:
        res += i + 1
print(res)
