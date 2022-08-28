from itertools import groupby


t = int(input())
for t in range(t):
    s, res = input(), "YES"
    for c, g in groupby(s):
        if sum(1 for i in g) == 1:
            res = "NO"
            break
    print(res)
