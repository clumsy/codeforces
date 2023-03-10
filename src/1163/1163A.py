n, m = (int(i) for i in input().split())
# optimal is to remove cats at every other position
# we can't have more groups than remaining cats
res = 1 if m == 0 else m if m <= n // 2 else n - m
print(res)
