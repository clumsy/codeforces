n = input()
res = n if n[0] != "-" else max(int(n[:-1]), int(n[:-2] + n[-1]))
print(res)
