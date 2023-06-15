from math import inf

n, x = int(input()), [int(i) for i in input().split()]
nxt_mi, mi = min(x), inf
while nxt_mi < mi:
    mi = nxt_mi
    for i in range(n):
        while x[i] > mi:
            x[i] -= mi
        nxt_mi = min(nxt_mi, x[i])
res = sum(x)
print(res)
