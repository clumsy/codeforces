from math import floor, log2

t = int(input())
for _ in range(t):
    n = int(input())
    # 2^highest_set_bit - 1
    res = 2 ** floor(log2(n)) - 1
    print(res)
