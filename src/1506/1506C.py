from math import inf

t = int(input())
for _ in range(t):
    a, b = (input() for _ in range(2))
    na, nb = len(a), len(b)
    res = inf
    for i in range(na):
        for j in range(nb):
            k = 0
            while i + k < na and j + k < nb and a[i + k] == b[j + k]:
                k += 1
            res = min(res, i + (na - (i + k)) + j + (nb - (j + k)))
    print(res)
