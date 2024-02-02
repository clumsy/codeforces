n = int(input())
# first vertex makes the most segments: n - 2
# the rest all make n - 3 each, we have n - 2 of them
# res = n - 2 + (n - 3) * (n - 2) = (n - 2) * (1 + n - 3)
res = (n - 2) ** 2
print(res)
