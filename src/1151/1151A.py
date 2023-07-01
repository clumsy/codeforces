from math import inf

n, s = int(input()), input()


def distance(a, b):
    a, b = sorted([ord(a), ord(b)])
    return min(b - a, a + 26 - b)


res = inf
for i in range(n - 3):
    res = min(res, sum(distance(a, b) for a, b in zip("ACTG", s[i : i + 4])))
print(res)
