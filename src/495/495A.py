from operator import mul
from functools import reduce

n = input()
m = {
    "0": 2,  # 0,8
    "1": 7,  # 0,1,3,4,7,8,9
    "2": 2,  # 2,8
    "3": 3,  # 3,8,9
    "4": 3,  # 4,8,9
    "5": 4,  # 5,6,8,9
    "6": 2,  # 6,8
    "7": 5,  # 0,3,7,8,9
    "8": 1,  # 8
    "9": 2,  # 8,9
}
res = reduce(mul, (m[c] for c in n))
print(res)
