a = input()
i = a.find("0")
res = a[:i] + a[i + 1 :] if i >= 0 else a[:-1]
print(res)
