from math import isqrt


t = int(input())
for _ in range(t):
    n = int(input())
    r = isqrt(n)
    res = r - (r * r == n)
    print(res)
#       |
#       |
#       |
# -------x------
#       |
#       |
#       |
# 1: 0

#       |
#       |
#       x
# ------x+x-----
#       x
#       |
#       |
# 2-4: 1

#       |
#       x
#      x|x
# -----x-x-x----
#      x|x
#       x
#       |
# 5-9: 2


#       x
#      x|x
#     x x x
# ----x-x+x-x----
#     x x x
#      x|x
#       x
# 10-16: 3

#       x
#       |
#       x
#       |
# ---x-x-x-x-x--
#       |
#       x
#       |
#       x
# 9: 4
