n, s = int(input()), input()
ones = s.count("1")
res = abs(ones - (n - ones))
print(res)
