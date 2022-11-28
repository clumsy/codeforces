s = input()
res = len(set(s.replace(",", "")[1:-1].split()))
print(res)
