n = int(input())
d, r = divmod(n, 4)
res = "aabb" * d + "aabb"[:r]
print(res)
