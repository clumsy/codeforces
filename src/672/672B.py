n, s = int(input()), input()
res = -1 if n > 26 else n - len(set(s))
print(res)
