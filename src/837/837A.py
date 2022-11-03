n, s = int(input()), input().split()
res = max(sum(c.isupper() for c in w) for w in s)
print(res)
