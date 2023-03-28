from math import floor, ceil

n, s = int(input()), input()
mid = (n - 1) / 2
res, j = [s[0]] * n, int(n & 1)
for i in range(j, ceil(mid) + j):
    res[floor(mid) - i] = s[j]
    res[ceil(mid) + i] = s[j + 1]
    j += 2
res = "".join(res)
print(res)
