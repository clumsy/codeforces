n, a = int(input()), input().replace(" ", "").strip("0")
res = a.count("1") + sum(len(x) == 1 for x in a.split("1"))
print(res)
